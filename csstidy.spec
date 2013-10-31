Summary:	Open Source CSS parser and optimiser
Summary(pl.UTF-8):	Analizator i optymalizator CSS z otwartymi źródłami
Name:		csstidy
Version:	1.4
Release:	2
License:	GPL v2+
Group:		Applications/WWW
Source0:	http://downloads.sourceforge.net/csstidy/%{name}-source-%{version}.zip
# Source0-md5:	8fcbf5c1c3cafd9232552b3286aabcb9
Source1:	http://ftp.debian.org/debian/pool/main/c/csstidy/%{name}_%{version}-3.diff.gz
# Source1-md5:	7087cc0c6cfdb42a3e796621a5d12a09
Patch0:		scons-optflags.patch
URL:		http://csstidy.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRequires:	scons
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
csstidy parses and optimises your CSS code, making it cleaner and more
concise. The end result is a smaller CSS file and better written code.
It has a variety of option settings giving the user a significant
amount of control over the level of file compression and readability.
It is not meant to be a CSS validator.

%description -l pl.UTF-8
csstidy analizuje i optymalizuje kod CSS, czyniąc go czystszym i
bardziej zwięzłym. Efekt końcowy to mniejszy plik CSS i lepiej
napisany kod. Ma rozmaite ustawienia opcji dające użytkowi znaczącą
kontrolę nad poziomem kompresji i czytelności pliku. Program nie jest
przeznaczony do sprawdzania poprawności CSS.

%prep
%setup -qcT
%{__unzip} -qq %{SOURCE0} || :
%{__gzip} -dc %{SOURCE1} | %{__patch} -p1
%{__patch} -p1 < debian/patches/001_emptyfile.dpatch
%{__patch} -p1 < debian/patches/002_gcc43fix.dpatch
%patch0 -p1

%build
%scons

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -p release/csstidy/csstidy $RPM_BUILD_ROOT%{_bindir}/csstidy
cp -a debian/csstidy.1 $RPM_BUILD_ROOT%{_mandir}/man1/csstidy.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/csstidy
%{_mandir}/man1/csstidy.1*
