---
slug: "mrk"
url: "/mobilnisite/slovnik/mrk/"
type: "slovnik"
title: "MRK – MBMS Request Key"
date: 2025-01-01
abbr: "MRK"
fullName: "MBMS Request Key"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/mrk/"
summary: "Kryptografický klíč používaný v zabezpečení služby Multimedia Broadcast Multicast Service (MBMS). Je generován BM-SC a poskytován autorizovaným uživatelům pro vyžádání klíčů služby MBMS, čímž zajišťuj"
---

MRK je MBMS Request Key, kryptografický klíč generovaný BM-SC a poskytovaný autorizovaným uživatelům pro bezpečné vyžádání klíčů služby MBMS (klíče pro přístup k vysílanému nebo multicastovanému obsahu).

## Popis

[MBMS](/mobilnisite/slovnik/mbms/) Request Key (MRK) je klíčový bezpečnostní prvek v architektuře služby Multimedia Broadcast Multicast Service (MBMS) dle 3GPP. Funguje jako sdílené tajemství mezi Broadcast Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)) a autorizovaným uživatelským zařízením (UE). MRK se nepoužívá přímo pro šifrování mediálního obsahu. Jeho primární role spočívá v zabezpečení doručení dalších nezbytných klíčů, konkrétně MBMS Traffic Key ([MTK](/mobilnisite/slovnik/mtk/)) a MBMS Service Key ([MSK](/mobilnisite/slovnik/msk/)), které se používají pro šifrování obsahu a autentizaci služby. BM-SC MRK vygeneruje a zřídí ho pro UE, která jsou oprávněna přijímat konkrétní službu MBMS, typicky jako součást procesu předplatného nebo aktivace služby.

Když se UE chce připojit ke službě MBMS, použije MRK v protokolu pro vyžádání klíče. UE typicky odešle žádost na BM-SC a tato žádost je autentizována pomocí MRK nebo klíčů z něj odvozených. Po úspěšné autentizaci BM-SC bezpečně doručí aktuální MTK a/nebo MSK žádajícímu UE. Toto doručení je často chráněno pomocí klíčů odvozených z MRK, což zajišťuje, že pouze UE disponující správným MRK mohou získat klíče potřebné k dešifrování vysílaného provozu. Tato dvouvrstvá hierarchie klíčů (MRK pro distribuci klíčů, MTK/MSK pro ochranu obsahu) poskytuje škálovatelnou a bezpečnou metodu pro správu přístupu ve vysílacích scénářích, kde je stejný obsah odesílán potenciálně milionům zařízení.

Správa MRK je centralizována v BM-SC. Jeho životní cyklus – generování, distribuce, případná obnova a odvolání – je řízen poskytovatelem služby. Bezpečnost celé služby MBMS závisí na důvěrnosti MRK. Pokud by byl kompromitován, útočník by mohl požadovat a získat platné klíče provozu, čímž by prolomil důvěrnost služby. Proto musí být MRK bezpečně uložen v odolném prostředí UE (jako je UICC) a přenášen pomocí zabezpečených kanálů během počátečního zřizování. Specifikace podrobně popisující MRK, jako je TS 33.246, definují funkce pro odvozování klíčů, velikosti klíčů a protokoly pro jeho použití v rámci bezpečnostního rámce MBMS.

## K čemu slouží

MRK byl vytvořen k řešení zásadní bezpečnostní výzvy škálovatelné ochrany obsahu v službách typu point-to-multipoint, jako je [MBMS](/mobilnisite/slovnik/mbms/). Tradiční modely bezpečnosti pro unicast, kde je jedinečný klíč sdílen mezi sítí a každým jednotlivým uživatelem, jsou pro vysílání neefektivní, protože by vyžadovaly, aby síť šifrovala stejný obsah miliony různých klíčů. MBMS potřebovalo model, kde by jeden šifrovaný proud mohl dešifrovat velká skupina autorizovaných uživatelů, ale kde by bylo možné kontrolovat přístup k dešifrovacímu klíči.

MRK to řeší zavedením vrstveného systému správy klíčů. Jeho účelem je fungovat jako stabilní dlouhodobá přihlašovací údaj, která ověřuje právo uživatele přijímat dynamické krátkodobé klíče používané pro skutečné dešifrování obsahu ([MTK](/mobilnisite/slovnik/mtk/)). Toto oddělení umožňuje častou změnu klíče obsahu (MTK) (např. na relaci nebo dokonce na film), aby se omezil dopad kompromitace klíče, aniž by to vyžadovalo nové zřízení dlouhodobých uživatelských přihlašovacích údajů (MRK). Bez MRK by neexistoval bezpečný a škálovatelný mechanismus pro distribuci klíčů provozu masivní, dynamické skupině účastníků, což by komerční vysílací služby činilo zranitelnými vůči pirátství a neoprávněnému přístupu.

## Klíčové vlastnosti

- Slouží jako dlouhodobé sdílené tajemství mezi BM-SC a autorizovaným UE pro přístup ke službě MBMS
- Používá se k autentizaci žádosti UE o dynamické klíče MBMS Traffic Keys (MTK) a Service Keys (MSK)
- Umožňuje zabezpečenou distribuci relakových klíčů prostřednictvím odvozování a šifrování klíčů
- Centralizované generování a správa Broadcast Multicast Service Center (BM-SC)
- Typicky zřizován do bezpečnostního prvku UE (např. UICC) během předplatného služby
- Tvoří základ dvouvrstvé hierarchie klíčů v zabezpečení MBMS

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [MTK – MBMS Traffic Key](/mobilnisite/slovnik/mtk/)
- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)
- [MUK – Multicast User Key](/mobilnisite/slovnik/muk/)
- [GBA – Generic Bootstrapping Architecture](/mobilnisite/slovnik/gba/)

## Definující specifikace

- **TS 33.246** (Rel-19) — MBMS Security Specification
- **TS 33.888** (Rel-12) — Security Study for Group Communication in LTE

---

📖 **Anglický originál a plná specifikace:** [MRK na 3GPP Explorer](https://3gpp-explorer.com/glossary/mrk/)
