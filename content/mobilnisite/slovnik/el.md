---
slug: "el"
url: "/mobilnisite/slovnik/el/"
type: "slovnik"
title: "EL – Echo Loss"
date: 2025-01-01
abbr: "EL"
fullName: "Echo Loss"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/el/"
summary: "Echo Loss (EL, útlum ozvěny) je klíčový metrický parametr kvality hlasu v 3GPP, který konkrétně měří útlum akustické ozvěny v komunikační cestě. Je zásadní pro zajištění čistých hlasových hovorů bez o"
---

EL je metrika kvality hlasu podle 3GPP, která měří útlum akustické ozvěny v komunikační cestě, aby kvantifikovala účinnost potlačení ozvěny a zajistila čisté hovory.

## Popis

Echo Loss (EL, útlum ozvěny) je základní parametr definovaný ve specifikacích 3GPP pro hodnocení a zajištění kvality hlasového přenosu. Kvantifikuje míru útlumu aplikovaného na akustickou ozvěnu, což je odraz hlasu mluvčího zpět do jeho vlastního sluchátka. Měření se provádí v referenčním bodu ucha ([ERP](/mobilnisite/slovnik/erp/)), standardizovaném akustickém rozhraní reprezentujícím uživatelovo ucho. EL je vyjádřen v decibelech (dB), přičemž vyšší hodnoty značí lepší potlačení ozvěny a tím i lepší vnímanou kvalitu hlasu. Metrika je nedílnou součástí testování výkonu a typového schvalování koncových zařízení, čímž zajišťuje, že zařízení splňují minimální kvalitativní prahy před nasazením.

Technické hodnocení Echo Loss zahrnuje řízené laboratorní testovací sestavy specifikované v dokumentech jako 3GPP TS 26.131 a TS 26.132. Tyto testy simulují reálné akustické podmínky, aby změřily, jak účinně hardware a software terminálu (včetně digitálních signálových procesorů) potlačují ozvěnu. Cesta ozvěny zahrnuje reproduktor terminálu, akustické prostředí a mikrofon. Hodnota EL je odvozena porovnáním úrovně testovacího signálu vyslaného do reproduktoru s úrovní téhož signálu zachyceného mikrofonem po průchodu touto cestou ozvěny a zpracování řídicími mechanismy potlačení ozvěny v terminálu.

V rámci širší síťové architektury je EL klíčovou součástí rámce pro správu kvality hlasu end-to-end. Zatímco uzly jádra sítě jako Media Gateway ([MGW](/mobilnisite/slovnik/mgw/)) implementují síťové potlačovače ozvěn, výkon na straně terminálu, měřený pomocí EL, je stejně důležitý. Špatné potlačení ozvěny na straně terminálu může přetížit síťové potlačovače a vést ke zhoršení kvality hovoru. Specifikace EL proto zajišťují základní výkonnost všech zařízení, což vytváří konzistentní a kvalitní uživatelský komfort v celé síti. Jeho definice v mnoha vydáních, od Rel-5 do Rel-19, podtrhuje jeho trvalý význam pro služby s přepojováním okruhů, Voice over LTE (VoLTE) a Voice over NR (VoNR).

## K čemu slouží

Hlavním účelem definice Echo Loss (EL, útlumu ozvěny) ve standardech 3GPP je bojovat proti škodlivému účinku akustické ozvěny na kvalitu hlasových hovorů. Ozvěna vzniká, když je hlas mluvčího z reproduktoru zachycen mikrofonem a přenesen zpět, čímž vznikne pro mluvčího zpožděná, rušivá ozvěna. Tento jev vážně degraduje uživatelský komfort a může ztížit konverzaci. Před standardizovanými metrikami, jako je EL, se výkonnost v potlačení ozvěn u různých výrobců terminálů značně lišila, což vedlo k nekonzistentní kvalitě hovorů a nespokojenosti uživatelů.

3GPP zavedlo EL ve vydání 5, aby stanovilo jednotné, objektivní a měřitelné kritérium pro akustický výkon terminálu. To bylo motivováno potřebou interoperability a garantovaného minimálního standardu kvality služeb s vývojem mobilních sítí. Specifikací testovacích metod a minimálních hodnot výkonu (např. v TS 26.131) 3GPP zajistilo, že všechna certifikovaná uživatelská zařízení poskytují základní úroveň potlačení ozvěny. Tato standardizace řeší problém nekvalitních zařízení, která podkopávají celkovou kvalitu hlasu v síti, a umožňuje síťovým operátorům poskytovat svým účastníkům spolehlivé, kvalitní hlasové služby. Řeší tak klíčové narušení na fyzické vrstvě v audio řetězci a doplňuje síťové potlačování ozvěn.

## Klíčové vlastnosti

- Kvantitativní metrika pro útlum akustické ozvěny měřená v decibelech (dB)
- Definována s odkazem na standardizovaný referenční bod ucha (ERP)
- Klíčový parametr pro testování akustického výkonu a typové schvalování terminálů
- Stanovuje minimální požadavky na výkon pro zajištění základní kvality hlasu
- Zahrnuje řízené laboratorní testování podle metodik 3GPP TS 26.131/132
- Použitelná pro služby hlasu s přepojováním okruhů, VoLTE a VoNR

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 26.115** (Rel-19) — 3GPP TS 26115: Echo Control Requirements
- **TS 26.131** (Rel-19) — Terminal Acoustic Performance Requirements
- **TS 26.132** (Rel-19) — Terminal Acoustic Test Methods
- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services
- **TS 43.050** (Rel-19) — GSM Transmission Planning for Speech Services

---

📖 **Anglický originál a plná specifikace:** [EL na 3GPP Explorer](https://3gpp-explorer.com/glossary/el/)
