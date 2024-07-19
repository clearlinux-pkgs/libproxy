#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v16
# autospec commit: 1bec16f
#
Name     : libproxy
Version  : 0.5.8
Release  : 13
URL      : https://github.com/libproxy/libproxy/archive/0.5.8/libproxy-0.5.8.tar.gz
Source0  : https://github.com/libproxy/libproxy/archive/0.5.8/libproxy-0.5.8.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: libproxy-bin = %{version}-%{release}
Requires: libproxy-data = %{version}-%{release}
Requires: libproxy-lib = %{version}-%{release}
Requires: libproxy-license = %{version}-%{release}
Requires: libproxy-man = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : curl-dev
BuildRequires : gi-docgen
BuildRequires : glib-dev
BuildRequires : gsettings-desktop-schemas
BuildRequires : pkgconfig(duktape)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-introspection-1.0)
BuildRequires : pkgconfig(gsettings-desktop-schemas)
BuildRequires : pkgconfig(libcurl)
BuildRequires : vala
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
![build](https://github.com/libproxy/libproxy/actions/workflows/build.yml/badge.svg)
[![codecov](https://codecov.io/github/libproxy/libproxy/branch/main/graph/badge.svg?token=UDbFtICyin)](https://codecov.io/github/libproxy/libproxy)
[![Coverity](https://github.com/libproxy/libproxy/actions/workflows/coverity.yml/badge.svg)](https://scan.coverity.com/projects/libproxy)
[![CodeQL](https://github.com/libproxy/libproxy/workflows/CodeQL/badge.svg)](https://github.com/libproxy/libproxy/actions?query=workflow%3ACodeQL)

%package bin
Summary: bin components for the libproxy package.
Group: Binaries
Requires: libproxy-data = %{version}-%{release}
Requires: libproxy-license = %{version}-%{release}

%description bin
bin components for the libproxy package.


%package data
Summary: data components for the libproxy package.
Group: Data

%description data
data components for the libproxy package.


%package dev
Summary: dev components for the libproxy package.
Group: Development
Requires: libproxy-lib = %{version}-%{release}
Requires: libproxy-bin = %{version}-%{release}
Requires: libproxy-data = %{version}-%{release}
Provides: libproxy-devel = %{version}-%{release}
Requires: libproxy = %{version}-%{release}

%description dev
dev components for the libproxy package.


%package doc
Summary: doc components for the libproxy package.
Group: Documentation
Requires: libproxy-man = %{version}-%{release}

%description doc
doc components for the libproxy package.


%package lib
Summary: lib components for the libproxy package.
Group: Libraries
Requires: libproxy-data = %{version}-%{release}
Requires: libproxy-license = %{version}-%{release}

%description lib
lib components for the libproxy package.


%package license
Summary: license components for the libproxy package.
Group: Default

%description license
license components for the libproxy package.


%package man
Summary: man components for the libproxy package.
Group: Default

%description man
man components for the libproxy package.


%prep
%setup -q -n libproxy-0.5.8
cd %{_builddir}/libproxy-0.5.8
pushd ..
cp -a libproxy-0.5.8 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1721420676
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :
cd ../buildavx2;
meson test -C builddir --print-errorlogs || : || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/libproxy
cp %{_builddir}/libproxy-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libproxy/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/proxy
/usr/bin/proxy

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Libproxy-1.0.typelib
/usr/share/gir-1.0/*.gir
/usr/share/vala/vapi/libproxy-1.0.deps
/usr/share/vala/vapi/libproxy-1.0.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/libproxy/proxy.h
/usr/lib64/libproxy.so
/usr/lib64/pkgconfig/libproxy-1.0.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/libproxy-1.0/RedHatDisplay-Black.woff
/usr/share/doc/libproxy-1.0/RedHatDisplay-Black.woff2
/usr/share/doc/libproxy-1.0/RedHatDisplay-BlackItalic.woff
/usr/share/doc/libproxy-1.0/RedHatDisplay-BlackItalic.woff2
/usr/share/doc/libproxy-1.0/RedHatDisplay-Bold.woff
/usr/share/doc/libproxy-1.0/RedHatDisplay-Bold.woff2
/usr/share/doc/libproxy-1.0/RedHatDisplay-BoldItalic.woff
/usr/share/doc/libproxy-1.0/RedHatDisplay-BoldItalic.woff2
/usr/share/doc/libproxy-1.0/RedHatDisplay-Italic.woff
/usr/share/doc/libproxy-1.0/RedHatDisplay-Italic.woff2
/usr/share/doc/libproxy-1.0/RedHatDisplay-Medium.woff
/usr/share/doc/libproxy-1.0/RedHatDisplay-Medium.woff2
/usr/share/doc/libproxy-1.0/RedHatDisplay-MediumItalic.woff
/usr/share/doc/libproxy-1.0/RedHatDisplay-MediumItalic.woff2
/usr/share/doc/libproxy-1.0/RedHatDisplay-Regular.woff
/usr/share/doc/libproxy-1.0/RedHatDisplay-Regular.woff2
/usr/share/doc/libproxy-1.0/RedHatText-Bold.woff
/usr/share/doc/libproxy-1.0/RedHatText-Bold.woff2
/usr/share/doc/libproxy-1.0/RedHatText-BoldItalic.woff
/usr/share/doc/libproxy-1.0/RedHatText-BoldItalic.woff2
/usr/share/doc/libproxy-1.0/RedHatText-Italic.woff
/usr/share/doc/libproxy-1.0/RedHatText-Italic.woff2
/usr/share/doc/libproxy-1.0/RedHatText-Medium.woff
/usr/share/doc/libproxy-1.0/RedHatText-Medium.woff2
/usr/share/doc/libproxy-1.0/RedHatText-MediumItalic.woff
/usr/share/doc/libproxy-1.0/RedHatText-MediumItalic.woff2
/usr/share/doc/libproxy-1.0/RedHatText-Regular.woff
/usr/share/doc/libproxy-1.0/RedHatText-Regular.woff2
/usr/share/doc/libproxy-1.0/SourceCodePro-It.ttf.woff
/usr/share/doc/libproxy-1.0/SourceCodePro-Regular.ttf.woff
/usr/share/doc/libproxy-1.0/SourceCodePro-Semibold.ttf.woff
/usr/share/doc/libproxy-1.0/applications.html
/usr/share/doc/libproxy-1.0/architecture.html
/usr/share/doc/libproxy-1.0/build-steps.html
/usr/share/doc/libproxy-1.0/classes_hierarchy.html
/usr/share/doc/libproxy-1.0/configuration-logic.html
/usr/share/doc/libproxy-1.0/ctor.ProxyFactory.new.html
/usr/share/doc/libproxy-1.0/fonts.css
/usr/share/doc/libproxy-1.0/fzy.js
/usr/share/doc/libproxy-1.0/go-up-symbolic.png
/usr/share/doc/libproxy-1.0/index.html
/usr/share/doc/libproxy-1.0/index.json
/usr/share/doc/libproxy-1.0/libproxy-1.0.devhelp2
/usr/share/doc/libproxy-1.0/libproxy.svg
/usr/share/doc/libproxy-1.0/main.js
/usr/share/doc/libproxy-1.0/method.ProxyFactory.free.html
/usr/share/doc/libproxy-1.0/method.ProxyFactory.get_proxies.html
/usr/share/doc/libproxy-1.0/perl.html
/usr/share/doc/libproxy-1.0/proxy-authentication.html
/usr/share/doc/libproxy-1.0/python.html
/usr/share/doc/libproxy-1.0/ruby.html
/usr/share/doc/libproxy-1.0/search.js
/usr/share/doc/libproxy-1.0/solarized-dark.css
/usr/share/doc/libproxy-1.0/solarized-light.css
/usr/share/doc/libproxy-1.0/struct.ProxyFactory.html
/usr/share/doc/libproxy-1.0/style.css
/usr/share/doc/libproxy-1.0/type_func.ProxyFactory.free_proxies.html
/usr/share/doc/libproxy-1.0/vala.html

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libproxy.so.0.5.8
/V3/usr/lib64/libproxy/libpxbackend-1.0.so
/usr/lib64/libproxy.so.0.5.8
/usr/lib64/libproxy.so.1
/usr/lib64/libproxy/libpxbackend-1.0.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libproxy/01a6b4bf79aca9b556822601186afab86e8c4fbf

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/proxy.8
