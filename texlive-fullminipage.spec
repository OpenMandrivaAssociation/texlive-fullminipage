%global tl_name fullminipage
%global tl_revision 34545

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1.1
Release:	%{tl_revision}.1
Summary:	Minipage spanning a complete page
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fullminipage
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fullminipage.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fullminipage.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fullminipage.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides the environment fullminipage, which generates a
minipage spanning a new, complete page with page style empty. The
environment provides options to set margins around the minipage and
configure the background.

