Summary: Tool for controlling tape drives
Name: mt-st
Version: 1.1
Release: 4%{?dist}
License: GPL+
Group: Applications/System
URL: ftp://ftp.ibiblio.org/pub/linux/system/backup
Source0: ftp://metalab.unc.edu/pub/Linux/system/backup/mt-st-%{version}.tar.gz
Source1: stinit.init
Patch0: mt-st-1.1-redhat.patch
Patch1: mt-st-1.1-SDLT.patch
Patch2: mt-st-0.7-config-files.patch
Patch3: mt-st-0.9b-manfix.patch
Patch4: mt-st-1.1-mtio.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires(post): chkconfig
Requires(preun): chkconfig

%description
The mt-st package contains the mt and st tape drive management
programs. Mt (for magnetic tape drives) and st (for SCSI tape devices)
can control rewinding, ejecting, skipping files and blocks and more.

Install mt-st if you need a tool to  manage tape drives.


%prep
%setup -q
%patch0 -p1 -b .redhat
%patch1 -p1 -b .sdlt
%patch2 -p1 -b .configfiles
%patch3 -p1 -b .manfix
%patch4 -p1 -b .mtio

# fix encoding
f=README.stinit
iconv -f ISO8859-1 -t UTF-8 -o $f.new $f
touch -r $f $f.new
mv $f.new $f


%build
make CFLAGS="$RPM_OPT_FLAGS"


%install
rm -rf $RPM_BUILD_ROOT
make install mandir=%{_mandir}
install -D -p -m 0755 %{SOURCE1} $RPM_BUILD_ROOT%{_initddir}/stinit


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/chkconfig --add stinit

%preun
if [ $1 -eq 0 ]; then
    /sbin/chkconfig --del stinit
fi


%files
%defattr(-,root,root,-)
%doc COPYING README README.stinit mt-st-1.1.lsm stinit.def.examples
/bin/mt
/sbin/stinit
%{_mandir}/man[18]/*
%{_initddir}/stinit


%changelog
* Tue Jan  5 2010 Dan Horák <dhorak@redhat.com> - 1.1-4
- stinit initscript updated (#541592)
- fixed License
- Related: rhbz#543948 

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.1-3.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Aug  4 2008 Dan Horak <dan[at]danny.cz> - 1.1-1
- update to upstream version 1.1
- rebase patches

* Mon May 26 2008 Radek Brich <rbrich@redhat.com> - 0.9b-6
- add init script to call /sbin/stinit (#249665)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9b-5
- Autorebuild for GCC 4.3

* Thu Aug 23 2007 Jindrich Novy <jnovy@redhat.com> - 0.9b-4
- update License
- rebuild for BuildID

* Wed Feb  7 2007 Jindrich Novy <jnovy@redhat.com> - 0.9b-3
- spec fixes
- use mtio.h from kernel-headers instead of the mt-st one

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.9b-2.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.9b-2.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.9b-2.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Oct 25 2005 Jindrich Novy <jnovy@redhat.com> 0.9b-2
- fix misleading description of "fsfm" and "bsfm" commands (#171340)

* Thu Sep 22 2005 Jindrich Novy <jnovy@redhat.com> 0.9b-1
- update to mt-st 0.9b

* Thu Apr  7 2005 Jindrich Novy <jnovy@redhat.com> 0.8-5
- add SDLT600 entry to stinit.def.examples,
  suggested by Ralf-Peter Rohbeck (#153305)

* Fri Mar  4 2005 Jindrich Novy <jnovy@redhat.com> 0.8-4
- rebuilt with gcc4

* Thu Feb 10 2005 Jindrich Novy <jnovy@redhat.com> 0.8-3
- remove -D_FORTIFY_SOURCE=2 from CFLAGS, present in RPM_OPT_FLAGS

* Wed Feb  9 2005 Jindrich Novy <jnovy@redhat.com> 0.8-2
- rebuilt with -D_FORTIFY_SOURCE=2

* Mon Aug 09 2004 Jindrich Novy <jnovy@redhat.com> 0.8-1
- updated to 0.8
- updated .redhat patch
- license fixup to GPL

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon May 26 2003 Than Ngo <than@redhat.com> 0.7-11.1
- add config file for Quantum DLT drive bug #91550

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sat Feb 22 2003 Than Ngo <than@redhat.com> 0.7-9
- add density code for Quantum SDLT320 from tibbs@math.uh.edu (#84843)

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Dec 11 2002 Tim Powers <timp@redhat.com> 0.7-7
- rebuild on all arches

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jun 19 2002 Than Ngo <than@redhat.com> 0.7-5
- don't forcibly strip binaries
- clean up a patch file

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Feb 26 2002 Than Ngo <than@redhat.com> 0.7-3
- rebuild

* Wed Feb 20 2002 Bernhard Rosenkraenzer <bero@redhat.com> 0.7-2
- Add density code 0x48 for Quantum SDLT220 tape drive (#59442)

* Tue Feb 19 2002 Bernhard Rosenkraenzer <bero@redhat.com> 0.7-1
- Update to 0.7

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Apr 24 2001 Than Ngo <than@redhat.com>
- update to 0.6, supports all ioctls up to kernel 2.4.0

* Thu Aug 17 2000 Jeff Johnson <jbj@redhat.com>
- summaries from specspo.

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Wed Jun 14 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging.

* Sat Apr 15 2000 Jeff Johnson <jbj@redhat.com>
- permit leading whitespace in config file.
- cortrect spelling error.

* Mon Feb  7 2000 Bill Nottingham <notting@redhat.com>
- handle compressed manpages

* Fri Jan 14 2000 Jeff Johnson <jbj@redhat.com>
- rebuild for Red Hat 6.2.

* Sun Sep  5 1999 Jeff Johnson <jbj@redhat.com>
- enable "datcompression" command (#3654).

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Wed Feb 10 1999 Preston Brown <pbrown@redhat.com>
- upgrade to .5b, which fixes some cmd. line arg issues (bugzilla #18)

* Thu Jul 23 1998 Jeff Johnson <jbj@redhat.com>
- package for 5.2.

* Sun Jul 19 1998 Andrea Borgia <borgia@cs.unibo.it>
- updated to version 0.5
- removed the touch to force the build: no binaries are included!
- added to the docs: README.stinit, stinit.def.examples
- made buildroot capable

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Oct 20 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Thu Jun 19 1997 Erik Troan <ewt@redhat.com>
- built against glibc
