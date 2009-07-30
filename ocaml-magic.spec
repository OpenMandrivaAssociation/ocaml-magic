Name:           ocaml-magic
Version:        0.7.3
Release:        %mkrel 1
Summary:        OCaml bindings for the File type determination library
License:        LGPL
Group:          Development/Other
URL:            http://sourceforge.net/projects/ocaml-magic/
Source0:        http://sourceforge.net/projects/ocaml-magic/files/ocaml-magic-0.7.3.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  libmagic-devel
BuildRequires:  ocaml-findlib

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

