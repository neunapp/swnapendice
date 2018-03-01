"use strict";
/*jshint esversion: 6 */

const gulp = require('gulp'),
      sass = require('gulp-sass'),
      plumber = require('gulp-plumber'),
      postcss = require('gulp-postcss'),
      autoprefixer = require('autoprefixer'),
      cssnano = require('cssnano'),
      browserSync = require('browser-sync'),
      exec = require('child_process').exec;

let postcssPlugins = [
  autoprefixer({
    browsers: 'last 3 versions',
    cascade: true
  }),
  //cssnano({core:true})
];

let sassOptions = {
  outputStyle: 'expanded'
};

gulp.task('styles', () =>
  gulp.src('./static/scss/**/*.scss')
      .pipe(plumber({
        errorHandler: function (err) {
          console.log(err);
          this.emit('end');
        }
      }))
      .pipe(sass(sassOptions))
      .pipe(postcss(postcssPlugins))
      .pipe(plumber.stop())
      .pipe(gulp.dest('./static/css'))
      .pipe(browserSync.reload({
        stream: true
      }))
);

gulp.task('runserver', function() {
  var proc = exec('python manage.py runserver --settings=napendice.settings.local');
});

gulp.task('browserSync', ['runserver'], function() {
  browserSync.init({
    notify: false,
    proxy: 'localhost:8000'
  });
});

gulp.task('watch', ['browserSync', 'styles'], function() {
  gulp.watch('./static/scss/**/*.scss', ['styles']);
  gulp.watch('./static/js/**/*.js', browserSync.reload);
  gulp.watch('./templates/**/*.html').on('change', browserSync.reload);
});
