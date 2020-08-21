const { parallel, src, dest } = require('gulp');
const postcss = require('gulp-postcss');
const bro = require('gulp-bro');
const rename = require('gulp-rename');

const css = (entrypoint, out) => {
  return () => {
    return src(entrypoint)
      .pipe(postcss([
        require('postcss-import'),
        require('postcss-nested'),
        require('autoprefixer'),
        require('cssnano')
      ]))
      .pipe(rename(out))
      .pipe(dest('../sphinxlectern/themes'));
  };
};

const js = (entrypoint, out) => {
  return () => {
    return src(entrypoint, {sourcemaps: true})
      .pipe(bro({
        transform: [
          ['uglifyify', {global: true}]
        ]
      }))
      .pipe(rename(out))
      .pipe(dest('../sphinxlectern/themes'));
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

exports.default = parallel(revealjs, handouts);