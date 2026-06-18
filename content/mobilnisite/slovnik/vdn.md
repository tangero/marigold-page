---
slug: "vdn"
url: "/mobilnisite/slovnik/vdn/"
type: "slovnik"
title: "VDN – VCC Domain Transfer Number"
date: 2025-01-01
abbr: "VDN"
fullName: "VCC Domain Transfer Number"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vdn/"
summary: "Telefonní číslo nebo identifikátor používaný v rámci Voice Call Continuity (VCC) pro usnadnění přenosu aktivního hlasového hovoru mezi doménou s přepojováním okruhů (CS) a doménou IP Multimedia Subsys"
---

VDN je telefonní číslo nebo identifikátor používaný v rámci architektury Voice Call Continuity pro směrování a přenos aktivního hlasového hovoru mezi přepojováním okruhů (circuit-switched domain) a doménou IMS.

## Popis

[VCC](/mobilnisite/slovnik/vcc/) Domain Transfer Number (VDN) je klíčový identifikátor v architektuře 3GPP Voice Call Continuity (VCC) specifikované ve vydání 7. VCC umožňuje plynulé předání hlasového hovoru mezi sítí s přepojováním okruhů (např. starší GSM/UMTS [CS](/mobilnisite/slovnik/cs/)) a paketovou sítí IMS (podporující VoIP). VDN je telefonní číslo, typicky číslo E.164, přiřazené VCC aplikaci v síti IMS. Slouží jako stabilní směrovací bod nebo kotva pro hovor během procesu přenosu mezi doménami.

Princip fungování: Když je UE s podporou VCC zapojeno do hlasového hovoru a potřebuje přenést hovor z domény CS do domény IMS (nebo naopak), síť zahájí proceduru přenosu domény. VDN se použije jako cílová adresa v této proceduře. Například při přenosu z CS do IMS je CS větev hovoru přesměrována (např. pomocí doplňkové služby GSM jako Explicit Call Transfer) na VDN. Tento hovor na VDN je směrován k VCC aplikaci v IMS. VCC aplikace, která VDN rozpozná a koreluje jej s kontextem probíhajícího hovoru, spojí příchozí CS větev s existující IMS větví, čímž přenos dokončí. VDN v podstatě poskytuje známý, statický kontaktní bod v IMS, na který může CS síť hovor 'předat'.

Mezi klíčové komponenty patří VCC aplikace ([SIP](/mobilnisite/slovnik/sip/) aplikační server v IMS), UE s VCC schopnostmi a jádrová síť CS ([MSC](/mobilnisite/slovnik/msc/)). VDN je nakonfigurován ve VCC aplikaci a je známý VCC logice UE. Jeho role je čistě pro síťové řízení a směrování během přenosu; není vytočeno koncovým uživatelem. Specifikace definují, jak je VDN zřízen, jak se používá v signalizaci (např. v SIP INVITE zprávách nebo [ISUP](/mobilnisite/slovnik/isup/) signalizaci) a jeho správu jako součást servisních dat předplatitele pro VCC.

## K čemu slouží

[VCC](/mobilnisite/slovnik/vcc/) Domain Transfer Number bylo vytvořeno k vyřešení technické výzvy plynulého přenosu aktivního hlasového hovoru mezi dvěma zásadně odlišnými síťovými doménami: doménou s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)) a paketovou doménou IP Multimedia Subsystem (IMS). Tato schopnost byla klíčová pro počáteční nasazení služeb Voice over IP (VoIP) založených na IMS, protože umožňovala operátorům nabídnout kontinuitu hlasové služby, když se uživatel pohyboval mezi oblastmi s pokrytím IMS (např. Wi-Fi nebo rané LTE) a starším pokrytím CS (2G/3G).

Bez mechanismu jako je VDN by přenos hovoru vyžadoval složité a netransparentní metody, jako je např. pozastavení jedné větve a založení nového hovoru, což by vedlo k přerušením, zpožděním a potenciálním ztrátám hovoru. VDN poskytuje standardizovaný, síťově řízený kotvící bod. Řeší problém směrování tím, že dává CS síti konkrétní číslo, na které má zavolat, aby 'našla' relaci hovoru založenou na IMS, což síti umožní obě větve z perspektivy uživatele plynule sloučit.

Historicky byly VCC a VDN klíčové ve vydání 7 jako součást snah o Fixed Mobile Convergence ([FMC](/mobilnisite/slovnik/fmc/)) a přípravu raného VoLTE. Řešily přechodné období, kdy CS a IMS hlasová služba koexistovaly. VDN umožnilo plynulý uživatelský zážitek pro duální telefony a podpořilo adopci IMS služeb. Ačkoli bylo později nahrazeno technologií Single Radio Voice Call Continuity (SRVCC) pro předání z LTE na 3G/2G, která používá jiné mechanismy, koncept VDN byl zásadní pro předvedení řízeného přenosu mezi doménami v rámci architektur 3GPP.

## Klíčové vlastnosti

- Číslo E.164 sloužící jako statická směrovací kotva pro VCC aplikaci v IMS
- Používá se jako cílová adresa pro přesměrování hovoru během přenosu domény z CS do IMS nebo z IMS do CS
- Umožňuje síťově řízenou, plynulou kontinuitu hovoru bez zásahu uživatele
- Konfigurováno jako součást servisních dat předplatitele ve VCC aplikaci
- Využíváno jak v CS signalizaci (např. ISUP), tak v IMS signalizaci (SIP) během přenosu
- Klíčové pro korelaci CS větve a IMS větve stejného koncová-koncová hovoru

## Definující specifikace

- **TS 23.206** (Rel-7) — Voice Call Continuity (VCC) Functional Architecture
- **TS 24.206** (Rel-7) — Voice Call Continuity Between CS and IMS
- **TS 24.216** (Rel-19) — Communication Continuity Management Object
- **TS 32.260** (Rel-19) — IMS Charging Management

---

📖 **Anglický originál a plná specifikace:** [VDN na 3GPP Explorer](https://3gpp-explorer.com/glossary/vdn/)
