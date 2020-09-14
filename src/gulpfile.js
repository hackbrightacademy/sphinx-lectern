const { parallel, src, dest, watch } = require('gulp');
const postcss = require('gulp-postcss');
const bro = require('gulp-bro');
const rename = require('gulp-rename');
const sass = require('gulp-sass');

sass.compiler = require('node-sass');

const sassBuild = () => {
  return src('./styles/bulma.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(dest('../docs/site/theme/static'));
};

const css = (entrypoint, out, destpath = '../sphinxlectern/themes') => {
  return () => {
    return src(entrypoint)
      .pipe(
        postcss([
          require('postcss-import'),
          require('postcss-nested'),
          require('autoprefixer'),
          require('cssnano'),
        ])
      )
      .pipe(rename(out))
      .pipe(dest(destpath));
  };
};

const js = (entrypoint, out, destpath = '../sphinxlectern/themes') => {
  return () => {
    return src(entrypoint, { sourcemaps: true })
      .pipe(
        bro({
          transform: [['uglifyify', { global: true }]],
        })
      )
      .pipe(rename(out))
      .pipe(dest(destpath));
  };
};

const revealjs = parallel(
  js('./scripts/revealjs.js', 'revealjs/static/main.js'),
  css('./styles/revealjs.css', 'revealjs/static/main.css')
);

const handouts = parallel(
  js('./scripts/handouts.js', 'handouts/static/main.js'),
  css('./styles/handouts.css', 'handouts/static/main.css')
);

const docs = parallel(
  js('./scripts/docs.js', 'static/main.js', '../docs/site/theme'),
  css('./styles/docs.css', 'static/main.css', '../docs/site/theme'),
  sassBuild
);

exports.watch = () => {
  return watch(
    ['./*.js', './*.css', './scripts/*', './styles/*'],
    parallel(revealjs, handouts, docs, sassBuild)
  );
};
exports.default = parallel(revealjs, handouts, docs);
