# Mengfei Zhao's website

The public site is https://mengfeizhao-math.github.io/.

Edit the page content in `build.py` and the styles in `site.css`. The portrait is at `assets/portrait.jpg` and the downloadable CV is at `files/Mengfei_Zhao_CV.pdf`, relative to the repository root.

From the repository root, run:

```sh
python3 simple-site/build.py --publish
```

Commit the source and the generated files at the repository root to `master`. GitHub Pages publishes the static files directly; `.nojekyll` disables the old Jekyll template build. Python is needed only for rebuilding the files, not for serving the site.

The six main pages are Home, Papers, Talks, Activities, CV, and Personal. The old `/publications/`, `/talks/`, `/cv/`, and `/teaching/` URLs redirect to their new pages. All paper links point to arXiv.

The legacy AcademicPages source remains in the repository history and existing directories. It is no longer used to generate the main pages.
