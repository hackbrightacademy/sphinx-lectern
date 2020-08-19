const { parallel, series, src, dest } = require('gulp');
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

// gulp.task('css', () => {
//   const plugins = [
//     require('postcss-import'),
//     require('postcss-nested'),
//     require('autoprefixer'),
//     require('cssnano')
//   ];

//   return gulp.src('./src/slides.css')
//     .pipe(postcss(plugins))
//     .pipe(gulp.dest('./static'));
// });

// gulp.task('copyCss', () => {
//   return gulp.src('./node_modules/reveal.js/css/reveal.css')
//     .pipe(gulp.dest('./static'));
// });

// gulp.task('scripts', () => {
//   return gulp.src('./src/slides.js')
//     .pipe(browserify({
//       insertGlobals: true
//     }))
//     .pipe(gulp.dest('./static/revealjs'))
// });

// gulp.task('default', gulp.parallel('css', 'copyCss', 'scripts'));
