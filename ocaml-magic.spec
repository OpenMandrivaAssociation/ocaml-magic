Name:           ocaml-magic
Version:        0.7.3
Release:        3
Summary:        OCaml bindings for the File type determination library
License:        LGPL
Group:          Development/Other
URL:            https://sourceforge.net/projects/ocaml-magic/
Source0:        http://sourceforge.net/projects/ocaml-magic/files/ocaml-magic-%{version}.tar.gz
BuildRequires:  magic-devel
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



%changelog
* Mon Aug 24 2009 Florent Monnier <blue_prawn@mandriva.org> 0.7.3-1mdv2010.1
+ Revision: 420284
- version var in source url

* Thu Jul 30 2009 Florent Monnier <blue_prawn@mandriva.org> 0.7.3-1mdv2010.0
+ Revision: 404486
- import ocaml-magic


