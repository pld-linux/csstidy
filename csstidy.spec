Summary:	Opensource CSS parser and optimiser
Name:		csstidy
Version:	1.2
Release:	0.3
License:	GPL v2
Group:		Applications/WWW
Source0:	http://dl.sourceforge.net/csstidy/%{name}-source-%{version}.zip
# Source0-md5:	cd2e1e50289fdaba0c56dcb293de8c40
Patch0:		http://ftp.debian.org/debian/pool/main/c/csstidy/%{name}_%{version}-1.diff.gz
URL:		http://csstidy.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
csstidy parses and optimises your CSS code, making it cleaner and more
concise. The end result is a smaller CSS file and better written code.
It has a variety of option settings giving the user a significant
amount of control over the level of file compression and readability.
It is not meant to be a css validator.

%prep
%setup -qc
%patch0 -p1
%{__patch} -p1 < debian/patches/01_Makefiles.dpatch
chmod +x configure

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -D csstidy.layout $RPM_BUILD_ROOT%{_datadir}/%{name}/csstidy.layout

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/csstidy
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/csstidy.layout
