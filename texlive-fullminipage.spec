Name:		texlive-fullminipage
Version:	34545
Release:	1
Summary:	Minipage spanning a complete page
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fullminipage
License:	gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fullminipage.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fullminipage.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fullminipage.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides the environment fullminipage, which
generates a minipage spanning a new, complete page with page
style empty. The environment provides options to set margins
around the minipage and configure the background.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/fullminipage
%{_texmfdistdir}/tex/latex/fullminipage
%doc %{_texmfdistdir}/doc/latex/fullminipage

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
