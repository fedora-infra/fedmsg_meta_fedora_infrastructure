Releasing fedmsg-met-fedora-infrastructure
==========================================

This document describes the process to follow when making a new release of
fedmsg-meta-fedora-infrastructure.

This projects uses the git-flow development model and tooling. You can find some
documentation about the model at the following URLs:

* https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow
* https://danielkummer.github.io/git-flow-cheatsheet/

Concretly:

* Install gitflow
::
    sudo dnf install gitflow

* Configure the git repo to follow the gitflow model (needed only once)
::
    git flow init

Here are the information you want for it:
- production release branch: `master`
- development branch: `develop`
- feature branch prefix: `feature/`
- release branch prefix: `release/`
- hotfix branch prefix: `hotfix/`
- support branch prefix: `support/`
- tag prefix: <empty>

* Start the release process:
::
    git flow release start <release number>
    git flow release start 0.28.0

* Update the `CHANGELOG.rst` file

* Adjust the version in `setup.py`

* Commit the resulting changes:
::
    git commit -asm "Release <release number>
    git commit -asm "Release 0.28.0"

* Finish the release:
::
    git flow release finish <release number>
    git flow release finish 0.28.0

* Write a message for the tag:
::
    Release <release number>
    Release 0.28.0

* Build the tarball
::
    python setup.py sdist

* Publish the tarball
::
    twine upload dist/<tarball>
    twine upload dist/fedmsg_meta_fedora_infrastructure-0.28.0.tar.gz

* Push the changes in git
::
    git push && git push --tags

* Push the changes in the master branch
::
    git checkout master
    git push

* Update the RPM in Fedora
