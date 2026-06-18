---
slug: "tspec"
url: "/mobilnisite/slovnik/tspec/"
type: "slovnik"
title: "TSPEC – Traffic Specification"
date: 2025-01-01
abbr: "TSPEC"
fullName: "Traffic Specification"
category: "QoS"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tspec/"
summary: "Soubor parametrů, které kvantitativně popisují charakteristiky provozu a požadavky na kvalitu služby (QoS) datového toku. Síť jej využívá k alokaci odpovídajících prostředků, provádění řízení přístupu"
---

TSPEC je soubor parametrů popisujících charakteristiky provozu a požadavky na kvalitu služby (QoS) datového toku, který síť využívá k alokaci prostředků a zajištění kvality služby.

## Popis

Specifikace provozu (Traffic Specification, TSPEC) je základním konceptem v architektuře kvality služby (QoS) 3GPP, který definuje charakteristiky a požadavky přenosového kanálu (beareru) nebo datového toku. Skládá se ze standardizované sady parametrů popisujících profil provozu od zdroje a očekávání QoS od sítě. Mezi klíčové parametry typicky patří garantovaný přenosový výkon ([GBR](/mobilnisite/slovnik/gbr/)), maximální přenosový výkon ([MBR](/mobilnisite/slovnik/mbr/)), rozpočet zpoždění paketů ([PDB](/mobilnisite/slovnik/pdb/)), míra ztráty paketů z důvodu chyb (PELR) a volitelně parametry tvarování provozu, jako je velikost burstu. TSPEC je generován aplikací nebo koncovým zařízením a je předán síti během procedur zřizování nebo modifikace přenosového kanálu, jako je aktivace kontextu [PDP](/mobilnisite/slovnik/pdp/) (Packet Data Protocol) v UMTS nebo zřizování [PDU](/mobilnisite/slovnik/pdu/) session v 5G.

Z architektonického hlediska je TSPEC zpracováván více síťovými funkcemi. V řídicí rovině přijímá TSPEC (často prostřednictvím aplikační funkce) funkce [PCRF](/mobilnisite/slovnik/pcrf/) (Policy and Charging Rules Function) v 4G nebo [PCF](/mobilnisite/slovnik/pcf/) (Policy Control Function) v 5G a využívá jej k odvození rozhodnutí o politice. Tato rozhodnutí jsou pak vynucována bránou [PGW](/mobilnisite/slovnik/pgw/) (Packet Gateway) nebo funkcí SMF (Session Management Function), která nařídí přístupové rádiové síti (RAN) a uzlům uživatelské roviny, aby odpovídajícím způsobem alokovaly prostředky. RAN využívá TSPEC pro plánování, řízení přístupu a konfiguraci linkové vrstvy za účelem splnění specifikovaného PDB a PELR.

Během provozu, když koncové zařízení (UE) požaduje službu, je přidružený TSPEC vyhodnocen vůči síťovým politikám a dostupným prostředkům. Síť provádí řízení přístupu, aby rozhodla, zda může požadovaný tok podporovat bez zhoršení stávajících služeb. Pokud je tok přijat, síť nakonfiguruje správu front, plánovací algoritmy a rádiové přenosové kanály tak, aby vyhovovaly TSPEC. Pro toky s GBR jsou vyhrazeny vyhrazené síťové prostředky, zatímco pro toky bez GBR (Non-GBR) jsou prostředky sdíleny statisticky. TSPEC umožňuje síti zacházet s různými typy provozu (např. hlas, video, provoz na pozadí) odpovídajícím způsobem a zajistit, aby aplikace citlivé na zpoždění dostaly přednost před daty s best-effort přístupem.

## K čemu slouží

TSPEC byl vytvořen za účelem umožnění diferencované kvality služby (QoS) v paketově přepínaných mobilních sítích, čímž řešil omezení raných datových služeb, které nabízely pouze jednotné, best-effort doručování. Jak se mobilní sítě vyvíjely, aby podporovaly rozmanité aplikace, jako je VoIP, streamované video a hry v reálném čase, z nichž každá má jedinečné požadavky na šířku pásma, zpoždění a spolehlivost, byl vyžadován mechanismus pro sdělení těchto požadavků síti za účelem správného zacházení s prostředky.

Zavedení TSPEC v UMTS Release 99 tento problém vyřešilo tím, že poskytlo standardizovaný způsob specifikace požadavků na provoz. Umožnilo síti implementovat inteligentní řízení přístupu a správu prostředků, čímž se zabránilo zahlcení a zajistil předvídatelný výkon prémiových služeb. Jednalo se o významný posun od jednotného přístupu, který umožnil operátorům nabízet služby ve vrstvách a zpeněžit QoS. V průběhu jednotlivých releasů se TSPEC vyvinul tak, aby podporoval složitější scénáře, jako je síťové dělení (network slicing) a edge computing, přičemž si zachoval svou roli základního deskriptoru pro QoS toky.

## Klíčové vlastnosti

- Definuje kvantitativní parametry provozu (GBR, MBR, PDB, PELR)
- Používá se pro síťové řízení přístupu a rezervaci prostředků
- Umožňuje diferencované zacházení s datovými toky na základě požadavků služby
- Standardizován napříč systémy 3GPP (UMTS, LTE, 5G)
- Integruje se s řízením politik (PCRF/PCF) pro dynamickou správu QoS
- Podporuje toky s garantovaným přenosovým výkonem (GBR) i bez něj (Non-GBR)

## Definující specifikace

- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS

---

📖 **Anglický originál a plná specifikace:** [TSPEC na 3GPP Explorer](https://3gpp-explorer.com/glossary/tspec/)
