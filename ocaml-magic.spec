Name:           ocaml-magic
Version:        0.7.3
Release:	6
Summary:        OCaml bindings for the File type determination library
License:        LGPL
Group:          Development/Other
URL:            https://sourceforge.net/projects/ocaml-magic/
Source0:	ocaml-magic-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	slibtool
BuildRequires:	make
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml

%description
Libmagic is a library for classifying files according to magic number tests.
This package provides OCaml interface to this C library.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n ocaml-magic-%{version}
# OCaml 5 C API
sed -i -e "s/\balloc_custom\b/caml_alloc_custom/g" 
       -e "s/\braise_out_of_memory\b/caml_raise_out_of_memory/g" 
       -e "s/\bcopy_string\b/caml_copy_string/g" 
       -e "s/\binvalid_argument\b/caml_invalid_argument/g" 
       -e "s/\braise_sys_error\b/caml_raise_sys_error/g" 
       -e "s/#include <caml\/mlvalues.h>/#include <caml\/mlvalues.h>\n#include <caml\/alloc.h>\n#include <caml\/memory.h>\n#include <caml\/fail.h>\n#include <caml\/custom.h>/" 
       magic_stubs.c

%build
%configure
make
make doc

%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/magic
make install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README
%dir %{_libdir}/ocaml/magic
%{_libdir}/ocaml/magic/META
%{_libdir}/ocaml/magic/*.cma
%{_libdir}/ocaml/magic/*.cmi
%{_libdir}/ocaml/stublibs/*.so*

%files devel
%defattr(-,root,root)
%doc doc
%{_libdir}/ocaml/magic/*.a
%{_libdir}/ocaml/magic/*.cmxa
%{_libdir}/ocaml/magic/*.cmx
%{_libdir}/ocaml/magic/*.mli
