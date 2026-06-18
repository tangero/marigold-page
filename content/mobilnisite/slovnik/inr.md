---
slug: "inr"
url: "/mobilnisite/slovnik/inr/"
type: "slovnik"
title: "INR – Implicit Neural Representation"
date: 2025-01-01
abbr: "INR"
fullName: "Implicit Neural Representation"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/inr/"
summary: "INR je technika komprese dat využívající neuronové sítě k reprezentaci multimediálního obsahu, jako jsou obrázky nebo video, jako spojité funkce. Umožňuje účinné ukládání a přenos tím, že se naučí kom"
---

INR je technika komprese dat, která využívá neuronové sítě k reprezentaci multimediálního obsahu jako spojité funkce pro účinné ukládání a přenos v mobilních sítích.

## Popis

Implicitní neuronová reprezentace (INR) je pokročilý paradigma komprese dat, které využívá neuronové sítě k parametrizaci multimediálních signálů. Na rozdíl od tradičních kodeků, které ukládají diskrétní hodnoty pixelů nebo transformační koeficienty, INR modeluje signál jako spojitou, diferencovatelnou funkci naučenou neuronovou sítí. Síť, typicky vícevrstvý perceptron ([MLP](/mobilnisite/slovnik/mlp/)), přijímá jako vstup prostorové nebo prostorově-časové souřadnice (např. x, y pro obrázek nebo x, y, t pro video) a na výstupu poskytuje odpovídající hodnotu signálu, jako je barva [RGB](/mobilnisite/slovnik/rgb/) nebo jas. Tato funkce je natrénována tak, aby aproximovala původní signál minimalizací ztráty rekonstrukce, což vede k souboru vah sítě, které slouží jako vysoce kompaktní reprezentace.

Architektura systému INR zahrnuje rámec kodér-dekodér, kde kodér může volitelně dále komprimovat váhy neuronové sítě a dekodér provede neuronovou síť pro rekonstrukci signálu. Klíčové komponenty zahrnují model neuronové sítě (často se sinusovým nebo pozičním kódováním pro zachycení vysokofrekvenčních detailů), tréninkový algoritmus (jako je zpětné šíření chyby) a modul kvantizace/entropického kódování pro váhy. V kontextech 3GPP je INR specifikována pro multimediální aplikace a umožňuje účinné streamování a ukládání snížením datových toků při zachování kvality.

Úlohou INR v mobilních sítích je zvýšit účinnost doručování multimédií. Reprezentací obsahu implicitně umožňuje škálovatelnou kvalitu, dekódování nezávislé na rozlišení a potenciál pro sémantickou kompresi. Neuronová reprezentace může být přenesena a následně na požádání dekódována na přijímači, přizpůsobujíc se možnostem zařízení. Tento přístup se integruje s existujícími multimediálními rámci 3GPP a nabízí novou alternativu ke konvenčním kodekům, jako je [AVC](/mobilnisite/slovnik/avc/) nebo [HEVC](/mobilnisite/slovnik/hevc/), zejména pro nové aplikace vyžadující vysoké kompresní poměry.

## K čemu slouží

INR byla zavedena k řešení rostoucích nároků na přenos multimediálních dat přes mobilní sítě s omezenou šířkou pásma. Tradiční kompresní metody, jako je bloková transformační kódování, čelí klesajícím výnosům a artefaktům při nízkých datových tocích. INR nabízí změnu paradigmatu využitím neuronových sítí k naučení spojité reprezentace, která může dosáhnout vyšší účinnosti komprese a lepší percepční kvality, zejména pro složité textury a detaily.

Motivace vychází z rozšíření videa s vysokým rozlišením, imerzních médií (např. [VR](/mobilnisite/slovnik/vr/)/[AR](/mobilnisite/slovnik/ar/)) a obsahu vytvářeného uživateli, což zatěžuje síťové zdroje. INR řeší problémy s režií úložiště a přenosu tím, že umožňuje kompaktnější reprezentace. Historicky předchozí přístupy spoléhaly na ručně vytvořené transformace a entropické kódování, které jsou méně adaptivní k obsahu. Na datech založená povaha INR jí umožňuje efektivněji zachytit složité vzory a redundance, čímž připravuje cestu pro multimediální služby příští generace v 5G a dalších sítích.

## Klíčové vlastnosti

- Spojitá reprezentace signálu prostřednictvím neuronových sítí
- Dekódování nezávislé na rozlišení a schopnost super-rozlišení
- Vysoká účinnost komprese pro složitý multimediální obsah
- Podpora různých typů signálů (obrázek, video, 3D)
- Integrace s multimediálními doručovacími protokoly 3GPP
- Adaptivní škálování kvality prostřednictvím prořezávání vah sítě

## Definující specifikace

- **TR 26.927** (Rel-19) — AI/ML in 5G Media Services Study
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 36.747** (Rel-14) — Enhanced CRS and SU-MIMO IM Performance Requirements

---

📖 **Anglický originál a plná specifikace:** [INR na 3GPP Explorer](https://3gpp-explorer.com/glossary/inr/)
