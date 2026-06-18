---
slug: "uaa"
url: "/mobilnisite/slovnik/uaa/"
type: "slovnik"
title: "UAA – User Authorization Answer"
date: 2025-01-01
abbr: "UAA"
fullName: "User Authorization Answer"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/uaa/"
summary: "Příkaz protokolu Diameter používaný v IP Multimedia Subsystem (IMS) jako odpověď na User Authorization Request (UAR). Je zasílán Home Subscriber Server (HSS) na Interrogating Call Session Control Func"
---

UAA je odpověď protokolu Diameter zaslaná HSS na I-CSCF v IMS za účelem autorizace registrace uživatele a poskytnutí adresy jeho přiřazeného S-CSCF.

## Popis

User Authorization Answer (UAA) je příkaz odpovědi protokolu Diameter definovaný ve specifikacích rozhraní Cx/Dx (TS 29.229, odkazováno přes TS 23.380) pro IP Multimedia Subsystem (IMS). Je to přímá odpověď na příkaz User Authorization Request ([UAR](/mobilnisite/slovnik/uar/)). UAA je zasílán z Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), což je centrální databáze uživatelů, na Interrogating Call Session Control Function ([I-CSCF](/mobilnisite/slovnik/i-cscf/)), což je vstupní kontaktní bod v domácí IMS síti. Hlavní funkcí UAA je předat rozhodnutí HSS ohledně žádosti uživatele o registraci v IMS síti a poskytnout potřebné směrovací informace.

Po přijetí UAR od [I-CSCF](/mobilnisite/slovnik/icscf/) provede HSS ověřovací a autorizační kontroly identity uživatele (Private User Identity a Public User Identity). HSS následně sestaví UAA, který obsahuje [AVP](/mobilnisite/slovnik/avp/) Result-Code indikující úspěch nebo selhání. V případě úspěšné autorizace nese UAA jeden nebo více klíčových atributů typu AVP (Attribute-Value Pair). Nejvýznamnějším z nich je AVP Server-Capabilities, který popisuje schopnosti, které musí mít [S-CSCF](/mobilnisite/slovnik/s-cscf/) obsluhující tohoto uživatele (např. podporované typy médií, povinné schopnosti). Případně, pokud byl pro uživatele již přiřazen konkrétní S-CSCF, může UAA obsahovat AVP Server-Name s přímou adresou ([FQDN](/mobilnisite/slovnik/fqdn/)) tohoto S-CSCF.

I-CSCF používá informace v UAA k výběru vhodného S-CSCF z fondu své sítě, který odpovídá schopnostem uvedeným HSS. Pokud je poskytnut Server-Name, I-CSCF jednoduše směruje registrační požadavek na tento konkrétní S-CSCF. UAA je tedy klíčovou zprávou, která umožňuje dynamické přiřazení S-CSCF, což je základní princip IMS umožňující vyrovnávání zátěže a přiřazení na základě služeb. Tento příkaz je výhradně součástí procedur registrace IMS a získávání počátečních filtračních kritérií, což z něj činí základní kámen pro zavedení přítomnosti uživatele a jeho servisního profilu v jádru IMS.

## K čemu slouží

Příkaz UAA existuje za účelem centralizace logiky autorizace uživatele a přiřazení [S-CSCF](/mobilnisite/slovnik/s-cscf/) v rámci architektury IMS. Řeší problém, jak může I-CSCF, který o uživateli nemá předchozí znalost, určit, kam směrovat registrační požadavek. Před IMS měly tradiční telefonní ústředny často statickou konfiguraci mapující uživatele na obslužné uzly, což bylo nepružné pro IP-based multimediální služby. Dialog UAA/UAR umožňuje dynamické přiřazení řízené politikami na základě uživatelského profilu a stavu sítě.

Vytvoření UAA bylo motivováno potřebou standardizované, bezpečné a škálovatelné metody pro ověřování uživatelů a jejich přiřazování k obslužnému uzlu (S-CSCF) schopnému obsluhovat jejich předplacené služby. Odděluje správu uživatelských dat (HSS) od směrování řízení relace (I-CSCF). Tento návrh umožňuje operátorům sítí nezávisle škálovat a spravovat fondy HSS a CSCF. UAA nese autoritativní rozhodnutí z HSS, čímž zajišťuje, že se mohou registrovat pouze autorizovaní uživatelé a že jsou přiřazeni k S-CSCF se schopnostmi nezbytnými pro provedení jejich servisní logiky, jako jsou interakce s telephony application server (TAS).

Jako příkaz založený na Diameteru také představuje vývoj od protokolu MAP založeného na SS7 používaného v jádrech s okruhovým přepojováním k IP-based protokolu vhodnému pro plně IP sítě. Jeho zavedení v Rel-8 se zarovnáním EPS/IMS bylo klíčové pro umožnění konvergence pevných a mobilních sítí a rich communication services přes LTE a následná 5G jádra.

## Klíčové vlastnosti

- Příkaz odpovědi protokolu Diameter (kód 300) na rozhraní Cx/Dx.
- Předává výsledek autorizace HSS pro registraci uživatele v IMS.
- Nese AVP Server-Capabilities pro výběr S-CSCF nebo AVP Server-Name pro přímé přiřazení.
- Obsahuje AVP Result-Code a Experimental-Result pro indikaci úspěchu nebo konkrétní chyby.
- Umožňuje dynamické přiřazení obslužného uzlu (S-CSCF) na základě schopností.
- Základní pro proceduru registrace IMS a nastavení počátečních filtračních kritérií.

## Související pojmy

- [UAR – User Authorization Request](/mobilnisite/slovnik/uar/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [I-CSCF – Interrogating-Call Session Control Function](/mobilnisite/slovnik/i-cscf/)
- [S-CSCF – Serving Call Session Control Function](/mobilnisite/slovnik/s-cscf/)

## Definující specifikace

- **TS 23.380** (Rel-19) — IMS Restoration Procedures

---

📖 **Anglický originál a plná specifikace:** [UAA na 3GPP Explorer](https://3gpp-explorer.com/glossary/uaa/)
