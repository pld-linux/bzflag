Summary:	multiplayer 3D tank battle game
Name:		bzflag
Version:	1.7d.9
Release:	3
Copyright:	Chris Schoeneman 1993-1999
Group:		X11/Games/Video
Source:		ftp://ftp.linuxgames.com/%{name}/src/%{name}-%{version}.src.tar.gz
Patch1:		bzflag-paths.patch
Patch2:		bzflag-opts.patch
URL:		http://bzflag.linuxgames.com
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
bzflag is a networked multiplayer 3D tank battle game, combining both fast
action and strategy. Free-for-all and capture-the-flag styles are
available.

%description -l pl
bzflag jest sieciow± gr± czo³gow± 3D, ³±cz±c± szybk± akcjê ze strategi±. 
Graæ mo¿na w wolnym stylu lub metod± "zdob±d¼ flagê".

%prep
%setup -qn bzflag
%patch1 -p1
%patch2 -p1

%build
make linux # other, arch-dependent targets differ only in optymalisation flags

COPTIMIZER="-DNDEBUG $RPM_OPT_FLAGS" \
CXXOPTIMIZER="-DNDEBUG $RPM_OPT_FLAGS" \
make

%install
install -d ${RPM_BUILD_ROOT}{%{_bindir},%{_datadir}/bzflag,%{_mandir}/man6}
install bin/* ${RPM_BUILD_ROOT}%{_bindir}
install man/*.6s ${RPM_BUILD_ROOT}%{_mandir}/man6
install data/* ${RPM_BUILD_ROOT}%{_datadir}/bzflag

gzip -9nf README BUGS RELNOTES TODO || :
gzip -9nf ${RPM_BUILD_ROOT}%{_mandir}/man6/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz BUGS.gz RELNOTES.gz TODO.gz 
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man6/*
%{_datadir}/bzflag
