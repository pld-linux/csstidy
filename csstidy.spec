Summary:	Opensource CSS parser and optimiser
Name:		csstidy
Version:	1.2
Release:	0.2
License:	GPL v2
Group:		Applications/WWW
Source0:	http://dl.sourceforge.net/csstidy/%{name}-source-%{version}.zip
# Source0-md5:	cd2e1e50289fdaba0c56dcb293de8c40
URL:		http://csstidy.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Opensource CSS parser and optimiser.

%prep
%setup -qc
sed -i -e 's,g++,%{__cxx},;s,-o,%{rpmcxxflags} -o,' compile.sh

%build
sh -x ./compile.sh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}
install csstidy $RPM_BUILD_ROOT%{_bindir}
cp -a csstidy.layout $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/csstidy
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/csstidy.layout
