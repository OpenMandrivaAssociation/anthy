%define	version   9100d
%define	release   %mkrel 1
%define	dic_date  071023

# b/c we include the .so for dlopen() in main lib package:
%define _requires_exceptions devel\(.*\) 

%define libname_orig lib%{name}
%define libname %mklibname %{name} 0
%define develname %mklibname -d %name

Name:      anthy
Summary:   A Japanese words input system
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   GPL
URL:       http://www.sourceforge.jp/projects/anthy/
Source0:   http://sourceforge.jp/projects/anthy/files/%{name}-%{version}.tar.gz

# http://sourceforge.jp/projects/alt-cannadic/files/
Source1:   alt-cannadic-%{dic_date}.tar.bz2

Requires:        %{libname} = %{version}
BuildRequires:   emacs-bin

%description
Anthy is a free and secure Japanese input system.


%package -n %{libname}
Summary:    Anthy library
Group:      System/Internationalization
Provides:   %{libname_orig} = %{version}-%{release}

%description -n %{libname}
Anthy library.

%package -n %{develname}
Summary:    Headers of %{name} for development
Group:      Development/C
Requires:   %{libname} = %{version}
Provides:   %{name}-devel = %{version}-%{release}
Provides:   %{libname_orig}-devel = %{version}-%{release}
Obsoletes:  %{libname}-devel

%description -n %{develname}
Anthy development package: static libraries, header files, and the like.


%prep
%setup -q

# update cannadic
cp %SOURCE1 .
tar -jxf %SOURCE1
cp alt-cannadic-%{dic_date}/*.ctd alt-cannadic

# remove an experimental dictionary
#rm alt-cannadic/gtankan-okuri.ctd

%build
%configure2_5x
# parallel doesn't work at the time.
make -j1

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog DIARY NEWS README doc
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/*
%{_datadir}/anthy
%{_datadir}/emacs/site-lisp/anthy/*

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/*.so.*
# (tv) fix uim dloading libanthy.so
%{_libdir}/*.so

%files -n %{develname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
