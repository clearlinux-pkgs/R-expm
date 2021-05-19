#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-expm
Version  : 0.999.6
Release  : 37
URL      : https://cran.r-project.org/src/contrib/expm_0.999-6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/expm_0.999-6.tar.gz
Summary  : Matrix Exponential, Log, 'etc'
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-expm-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
and related quantities, using traditional and modern methods.

%package lib
Summary: lib components for the R-expm package.
Group: Libraries

%description lib
lib components for the R-expm package.


%prep
%setup -q -c -n expm
cd %{_builddir}/expm

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1610555823

%install
export SOURCE_DATE_EPOCH=1610555823
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library expm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library expm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library expm
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc expm || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/expm/DESCRIPTION
/usr/lib64/R/library/expm/INDEX
/usr/lib64/R/library/expm/Meta/Rd.rds
/usr/lib64/R/library/expm/Meta/data.rds
/usr/lib64/R/library/expm/Meta/demo.rds
/usr/lib64/R/library/expm/Meta/features.rds
/usr/lib64/R/library/expm/Meta/hsearch.rds
/usr/lib64/R/library/expm/Meta/links.rds
/usr/lib64/R/library/expm/Meta/nsInfo.rds
/usr/lib64/R/library/expm/Meta/package.rds
/usr/lib64/R/library/expm/Meta/vignette.rds
/usr/lib64/R/library/expm/NAMESPACE
/usr/lib64/R/library/expm/R/expm
/usr/lib64/R/library/expm/R/expm.rdb
/usr/lib64/R/library/expm/R/expm.rdx
/usr/lib64/R/library/expm/data/matStig.R
/usr/lib64/R/library/expm/demo/balanceTst.R
/usr/lib64/R/library/expm/demo/exact-fn.R
/usr/lib64/R/library/expm/demo/expm.R
/usr/lib64/R/library/expm/doc/expm.R
/usr/lib64/R/library/expm/doc/expm.Rnw
/usr/lib64/R/library/expm/doc/expm.pdf
/usr/lib64/R/library/expm/doc/index.html
/usr/lib64/R/library/expm/help/AnIndex
/usr/lib64/R/library/expm/help/aliases.rds
/usr/lib64/R/library/expm/help/expm.rdb
/usr/lib64/R/library/expm/help/expm.rdx
/usr/lib64/R/library/expm/help/paths.rds
/usr/lib64/R/library/expm/html/00Index.html
/usr/lib64/R/library/expm/html/R.css
/usr/lib64/R/library/expm/po/en@quot/LC_MESSAGES/R-expm.mo
/usr/lib64/R/library/expm/po/en@quot/LC_MESSAGES/expm.mo
/usr/lib64/R/library/expm/po/fr/LC_MESSAGES/expm.mo
/usr/lib64/R/library/expm/po/fr/LC_MESSAGES/fr.mo
/usr/lib64/R/library/expm/test-tools.R
/usr/lib64/R/library/expm/tests/Frechet-test.R
/usr/lib64/R/library/expm/tests/bal-ex.R
/usr/lib64/R/library/expm/tests/ex.R
/usr/lib64/R/library/expm/tests/ex2.R
/usr/lib64/R/library/expm/tests/exact-ex.R
/usr/lib64/R/library/expm/tests/expm-Cond.R
/usr/lib64/R/library/expm/tests/log+sqrt.R
/usr/lib64/R/library/expm/tests/matpow-ex.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/expm/libs/expm.so
/usr/lib64/R/library/expm/libs/expm.so.avx2
/usr/lib64/R/library/expm/libs/expm.so.avx512
