%define dic_date  20110409

%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Name:		anthy
Summary:	A Japanese words input system
Version:	9100h
Release:	25.%{dic_date}.3
Group:		System/Internationalization
License:	GPLv2+
URL:		http://www.geocities.jp/ep3797/index.html
# http://www.geocities.jp/ep3797/anthy_dict_01.html
Source0:	http://ovh.dl.sourceforge.net/sourceforge/mdk-ut/anthy/anthy-%{version}-%{dic_date}ut.tar.bz2

Requires:	%{libname} = %{version}-%{release}
BuildRequires:	emacs-bin
BuildRequires:	automake

%description
Anthy is a free and secure Japanese input system.

%package -n %{libname}
Summary:	Anthy library
Group:		System/Libraries

%description -n %{libname}
Anthy library.

%package -n %{develname}
Summary:	Headers of %{name} for development
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Anthy development package: .so libraries, header files, and the like.

%prep
%setup -q -n %{name}-%{version}-%{dic_date}ut

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog DIARY NEWS README doc
%{_bindir}/*
%config %{_sysconfdir}/*
%{_datadir}/anthy
%{_datadir}/emacs/site-lisp/anthy/*

%files -n %{libname}
%doc COPYING
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc COPYING
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*

%changelog
* Mon May 02 2011 Funda Wang <fwang@mandriva.org> 9100h-25.20110409.1
+ Revision: 662337
- use patched sources

* Mon Aug 09 2010 Funda Wang <fwang@mandriva.org> 9100h-25.20100710.1mdv2011.0
+ Revision: 567855
- sync with ut packages

* Tue May 25 2010 Christophe Fergeau <cfergeau@mandriva.com> 9100h-21.20100423.3mdv2010.1
+ Revision: 545958
- fix anthy crash when HOME isn't set

* Wed Apr 28 2010 Christophe Fergeau <cfergeau@mandriva.com> 9100h-21.20100423.2mdv2010.1
+ Revision: 540236
- rebuild so that shared libraries are properly stripped again

* Mon Apr 26 2010 Funda Wang <fwang@mandriva.org> 9100h-21.20100423.1mdv2010.1
+ Revision: 538822
- New patch seriers

* Fri Jan 29 2010 Funda Wang <fwang@mandriva.org> 9100h-20.20091228.1mdv2010.1
+ Revision: 497934
- use patches anthy sources

* Mon Nov 09 2009 Funda Wang <fwang@mandriva.org> 9100h-11.20091030.1mdv2010.1
+ Revision: 463358
- New ut patches

* Thu Oct 08 2009 Funda Wang <fwang@mandriva.org> 9100h-11.20091001.1mdv2010.0
+ Revision: 456124
- New ut patches

* Fri Sep 25 2009 Olivier Blin <oblin@mandriva.com> 9100h-11.20090731.1mdv2010.0
+ Revision: 448776
- fix long double brain damage since on some ABI, long double = double
  (rediffed patch from Arnaud Patard)

* Sat Aug 01 2009 Funda Wang <fwang@mandriva.org> 9100h-10.20090731.1mdv2010.0
+ Revision: 405356
- new ut patches

* Sat Jul 11 2009 Funda Wang <fwang@mandriva.org> 9100h-10.20090704.1mdv2010.0
+ Revision: 394434
- New ut patches

* Sat May 30 2009 Funda Wang <fwang@mandriva.org> 9100h-1.20090507.1mdv2010.0
+ Revision: 381397
- New ut patches

* Mon Feb 09 2009 Funda Wang <fwang@mandriva.org> 9100h-1.20090209.1mdv2009.1
+ Revision: 338763
- reconf
- New version 9100h with newer ut patches

* Sat Feb 07 2009 Funda Wang <fwang@mandriva.org> 9100g-1.20090129.1mdv2009.1
+ Revision: 338323
- disable ut patches for now (it modifies configure.ac too much)
- anthy 9100g
- New ut patches

* Mon Jan 19 2009 Funda Wang <fwang@mandriva.org> 9100e-18.20090119.1mdv2009.1
+ Revision: 331285
- fix str fmt
- new patches

* Mon Dec 08 2008 Funda Wang <fwang@mandriva.org> 9100e-17.20081203.1mdv2009.1
+ Revision: 311860
- new patch series

* Thu Nov 20 2008 Funda Wang <fwang@mandriva.org> 9100e-16.20081117.1mdv2009.1
+ Revision: 304928
- new ut patches

* Sat Oct 25 2008 Funda Wang <fwang@mandriva.org> 9100e-15.20081025.1mdv2009.1
+ Revision: 297231
- new ut patches

* Mon Oct 20 2008 Funda Wang <fwang@mandriva.org> 9100e-14.20081018.1mdv2009.1
+ Revision: 295473
- new ut patches 20081018

* Thu Oct 16 2008 Funda Wang <fwang@mandriva.org> 9100e-13.20081015.1mdv2009.1
+ Revision: 294111
- New ut patches

* Sun Sep 28 2008 Funda Wang <fwang@mandriva.org> 9100e-12.20080928.1mdv2009.0
+ Revision: 288969
- New ut patches

* Mon Aug 04 2008 Funda Wang <fwang@mandriva.org> 9100e-11.20080804.1mdv2009.0
+ Revision: 263386
- new ut patches

* Sun Jun 15 2008 Funda Wang <fwang@mandriva.org> 9100e-10.20080605.1mdv2009.0
+ Revision: 219205
- move .so file into devel package

* Sun Jun 15 2008 Funda Wang <fwang@mandriva.org> 9100e-9.20080605.1mdv2009.0
+ Revision: 219204
- New ut patches

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sat May 03 2008 Funda Wang <fwang@mandriva.org> 9100e-8.20080502.1mdv2009.0
+ Revision: 200586
- New ut patches

* Mon Apr 21 2008 Funda Wang <fwang@mandriva.org> 9100e-7.20080411.1mdv2009.0
+ Revision: 196293
- Updated ut patches

* Fri Mar 14 2008 Funda Wang <fwang@mandriva.org> 9100e-7.20080309.1mdv2008.1
+ Revision: 187754
- Update ut patches

* Sat Mar 08 2008 Funda Wang <fwang@mandriva.org> 9100e-6.20080226.1mdv2008.1
+ Revision: 182054
- Updated ut patches

* Tue Feb 26 2008 Funda Wang <fwang@mandriva.org> 9100e-5.20080224.1mdv2008.1
+ Revision: 175232
- Update patches from ut

* Sat Feb 09 2008 Funda Wang <fwang@mandriva.org> 9100e-4mdv2008.1
+ Revision: 164435
- Updatedut patches

* Thu Feb 07 2008 Funda Wang <fwang@mandriva.org> 9100e-3mdv2008.1
+ Revision: 163396
- Updated patches from UTUMI Hirosi

* Tue Jan 29 2008 Funda Wang <fwang@mandriva.org> 9100e-2mdv2008.1
+ Revision: 159831
- disable non-applied patch
- Use new patch

* Tue Jan 29 2008 Funda Wang <fwang@mandriva.org> 9100e-1mdv2008.1
+ Revision: 159595
- New version 9100e

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Nov 02 2007 Funda Wang <fwang@mandriva.org> 9100d-1mdv2008.1
+ Revision: 105270
- New version 9100d

* Sat Oct 27 2007 Funda Wang <fwang@mandriva.org> 9100c-1mdv2008.1
+ Revision: 102562
- Drop unused patches
- New version 9100c

* Wed Aug 29 2007 Funda Wang <fwang@mandriva.org> 9100-2mdv2008.0
+ Revision: 74998
- Merge UTUMI Hirosi's changes

* Sat Jul 07 2007 Funda Wang <fwang@mandriva.org> 9100-1mdv2008.0
+ Revision: 49345
- New version

* Sat Jun 16 2007 Funda Wang <fwang@mandriva.org> 9011-1mdv2008.0
+ Revision: 40364
- New version

* Mon May 28 2007 Funda Wang <fwang@mandriva.org> 8921-1mdv2008.0
+ Revision: 31907
- New version

* Sun May 13 2007 Funda Wang <fwang@mandriva.org> 8906-1mdv2008.0
+ Revision: 26504
- New upstream version

* Wed Apr 25 2007 Funda Wang <fwang@mandriva.org> 8819-1mdv2008.0
+ Revision: 18087
- emacs scripts location has changed.
- New upstream version.
  parallel build doesn't build.

* Mon Apr 23 2007 Funda Wang <fwang@mandriva.org> 8700b-1mdv2008.0
+ Revision: 17174
- New upstream version 8700b.


* Fri Nov 24 2006 Thierry Vignaud <tvignaud@mandriva.com> 8300-1mdv2007.0
+ Revision: 87014
- UTUMI Hirosi <utuhiro78@yahoo.co.jp>:
- new release
- update source1 (anthy_gcanna_ut)
- add patch0 (it will be merged soon)
- reenable parallel build

* Wed Oct 18 2006 Thierry Vignaud <tvignaud@mandriva.com> 8116-1mdv2007.1
+ Revision: 65971
- temporary disable broken parallel build
- new release; update source1 (UTUMI Hirosi <utuhiro78@yahoo.co.jp>)
- initial import
- Created package structure for anthy.

* Fri Sep 01 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 8023-1mdv2007.0
- new release
- update source1 (anthy_gcanna_ut)

* Wed Aug 30 2006 Thierry Vignaud <tvignaud@mandriva.com> 8019-2mdv2007.0
- prevent extra devel requires on non devel file

* Tue Aug 22 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 8019-1mdv2007.0
- new release
- update source1 (anthy_gcanna_ut)
- remove patch0,1 (merged upstream)

* Thu Aug 17 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 8013-2mdv2007.0
- update source1 (anthy_gcanna_ut)
- add patch0 (anthy-name.t_20060815.diff)
- add patch1 (anthy_gcannaf.ctd_20060815.diff)

* Tue Aug 15 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 8013-1mdv2007.0
- new release

* Tue Aug 01 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 7929-1mdv2007.0
- new release

* Tue Jul 25 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 7917-1mdv2007.0
- new release

* Tue Jun 20 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 7818-1mdv2007.0
- new release

* Mon May 15 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 7714-1mdk
- new release

* Thu Apr 27 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 7625-1mdk
- new release

* Thu Apr 27 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 7625-1mdk
- new release

* Sun Apr 23 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 7622-1mdk
- new release

* Thu Apr 20 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 7614-2mdk
- update source1

* Sun Apr 16 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 7614-1mdk
- new release
- remove patch0 (merged upstream)

* Fri Apr 14 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 7608-1mdk
- new release
- update source1
- remove patch0, patch1 (merged upstream)
- add new patch0

* Wed Mar 15 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 7500-1mdk
- new release
- remove patch0 (merged upstream)
- update source1
- add patch0
- add patch1

* Wed Feb 22 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 7419-2mdk
- update source1
- update patch0

* Tue Feb 21 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 7419-1mdk
- new release
- update source1
- add patch0

* Sun Jan 08 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 7307-1mdk
- replace patch0 with source1
- update source1 (cannadic)

* Wed Dec 28 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 7227-1mdk
- new release
- update patch0

* Tue Nov 22 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 7100b-2mdk
- remove source1 (anthy_placename) to keep conversion compatibility

* Thu Nov 03 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 7100b-1mdk
- new release

* Sun Oct 30 2005 Nicolas l?ureuil <neoclust@mandriva.org> 7029-1mdk
- package from : UTUMI Hirosi <utuhiro78 at yahoo dot co dot jp>
	- new release
	- add patches for dictionaries (source1, patch0)

* Fri Oct 07 2005 Thierry Vignaud <tvignaud@mandriva.com> 6829-1mdk
- new release

* Thu Aug 04 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 6801-1mdk
- new release

* Sat Jul 23 2005 Nicolas L?ureuil <neoclust@mandriva.org> 6700b-1mdk
- New release 6700b

* Sat Jun 18 2005 Nicolas L?ureuil <neoclust@mandriva.org> 6606-1mdk
- New release 6606

* Tue May 10 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 6508-1mdk
- new release

* Sun Apr 03 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 6331-1mdk
- new release

* Tue Mar 08 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 6300d-1mdk
- new release

* Sun Mar 06 2005 Stefan van der Eijk <stefan@eijk.nu> 6300-2mdk
- reupload, src.rpm got lost
- remove requires-on-release (rpmlint)

* Mon Feb 28 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 6300-1mdk
- new release
- spec clean up

* Tue Feb 01 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 6131-1mdk
- new release (fix conversion quite a lot common japanese words)

* Fri Jan 28 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 6125-1mdk
- new release

* Tue Dec 28 2004 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 6024-1mdk
- new release
- clean up spec

* Thu Nov 25 2004 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 5924-1mdk
- new release

* Mon Nov 01 2004 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 5900-1mdk
- new release

* Thu Sep 16 2004 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 5714-1mdk
- new release

* Sun Sep 05 2004 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 5704-1mdk
- new release

* Sat Aug 28 2004 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 5626-1mdk
- new release

* Fri Aug 06 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 5605-1mdk
- new release
- reenable libtoolize

* Sun Aug 01 2004 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 5531-1mdk
- new release

* Fri Jul 30 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 5524-2mdk
- rpmbuildupdate aware

* Sun Jul 25 2004 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 5524-1mdk
- new release

* Sun Jul 25 2004 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 5523-1mdk
- new release

* Wed Jul 21 2004 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 5516-1mdk
- new release

* Tue Jun 22 2004 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 5414-1mdk
- new release

* Wed Jun 09 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 5406-1mdk
- new release

* Fri May 28 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 5326-1mdk
- new release

* Sat Apr 03 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 5100-1mdk
- new release

* Thu Feb 26 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 4925-5mdk
- move .so link into libanthy0 since uim load them through dlopen

* Wed Feb 18 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 4925-4mdk
- fix requires

* Wed Feb 18 2004 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 4925-3mdk
- fix requires

* Fri Jan 30 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 4925-2mdk
- use proper build fix

* Thu Jan 29 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 4925-1mdk
- new release
- fix build

* Sat Jan 24 2004 Per ?vind Karlsen <peroyvind@linux-mandrake.com> 4700-2mdk
- fix buildrequires
- cosmetics

* Wed Jan 21 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 4700-1mdk
- from UTUMI Hirosi <utuhiro78@yahoo.co.jp>: initial upload

