Summary:	RIGS - Ruby Interface for GNUstep
Summary(pl.UTF-8):	RIGS - Interfejs Ruby do GNUstepa
Name:		gnustep-ruby
Version:	0.2.2
Release:	1
License:	LGPL/GPL
Group:		Libraries
Source0:	ftp://ftp.gnustep.org/pub/gnustep/libs/rigs-%{version}.tar.gz
# Source0-md5:	d6e0231311f1822f8981014a0cf6cffc
#Source0:	%{name}-cvs-%{cvs}.tar.gz
Patch0:		%{name}-link.patch
Patch1:		%{name}-rootdir.patch
URL:		http://www.gnustep.org/experience/RIGS.html
BuildRequires:	gnustep-base-devel >= 1.7.1
BuildRequires:	gnustep-gui-devel >= 0.8.6
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel >= 1:1.6.4
Requires:	gnustep-base >= 1.7.1
Requires:	gnustep-gui >= 0.8.6
Requires:	ruby >= 1:1.6.4
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gsdir		/usr/%{_lib}/GNUstep

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%(echo %{_target_cpu} | sed -e 's/amd64/x86_64/;s/ppc/powerpc/')
%endif

%description
RIGS stands for Ruby Interface for GNUstep. It is a package allowing
integration between Ruby and Objective-C/GNUstep. The main purpose of
RIGS is to allow the use the GNUstep development environment from
Ruby.

%description -l pl.UTF-8
RIGS to interfejs Ruby do GNUstepa. Pakiet ten umożliwia integrację
między językiem Ruby a Objective-C i GNUstepem. Głównym celem RIGS
jest umożliwienie używania środowiska GNUstep z poziomu języka Ruby.

%prep
%setup -q -n rigs-%{version}
%patch0 -p1
%patch1 -p1

%build
. %{_gsdir}/System/Library/Makefiles/GNUstep.sh

%{__make} \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_gsdir}/System/Library/Makefiles/GNUstep.sh
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
%attr(755,root,root) %{ruby_sitearchdir}/librigs.so
%{ruby_sitelibdir}/*.rb
%{ruby_sitelibdir}/rigs

# GNUstep world
%attr(755,root,root) %{_gsdir}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/lib*.so.*
