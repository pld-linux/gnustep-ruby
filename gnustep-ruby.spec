Summary:	RIGS - Ruby Interface for GNUstep
Summary(pl):	RIGS - Interfejs Ruby do GNUstepa
Name:		gnustep-ruby
Version:	0.2.1
Release:	1
License:	LGPL/GPL
Group:		Libraries
Source0:	ftp://ftp.gnustep.org/pub/gnustep/libs/%{name}-%{version}.tgz
# Source0-md5:	2adb1444179d47566aa7dd5730c789ba
Patch0:		%{name}-link.patch
Patch1:		%{name}-rootdir.patch
URL:		http://www.gnustep.org/
BuildRequires:	gnustep-base-devel
BuildRequires:	gnustep-gui-devel
BuildRequires:	ruby >= 1.6.4
Requires:	ruby >= 1.6.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gsdir		/usr/lib/GNUstep

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%{_target_cpu}
%endif

%description
RIGS stands for Ruby Interface for GNUstep. It is a package allowing
integration between Ruby and Objective-C/GNUstep. The main purpose of
RIGS is to allow the use the GNUstep development environment from
Ruby.

%description -l pl
RIGS to interfejs Ruby do GNUstepa. Pakiet ten umo¿liwia integracjê
miêdzy jêzykiem Ruby a Objective-C i GNUstepem. G³ównym celem RIGS
jest umo¿liwienie u¿ywania ¶rodowiska GNUstep z poziomu jêzyka Ruby.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
. %{_gsdir}/System/Makefiles/GNUstep.sh

%{__make} \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_gsdir}/System/Makefiles/GNUstep.sh
%{__make} install \
	INSTALL_ROOT_DIR=$RPM_BUILD_ROOT \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_gsdir}/System

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO

# UNIX world
%attr(755,root,root) %{_libdir}/ruby/site_ruby/*/*-linux/librigs.so
%{_libdir}/ruby/site_ruby/*/*.rb
%{_libdir}/ruby/site_ruby/*/rigs

# GNUstep world
%attr(755,root,root) %{_gsdir}/System/Libraries/%{gscpu}/%{gsos}/%{libcombo}/lib*.so.*
