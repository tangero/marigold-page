---
slug: "lia"
url: "/mobilnisite/slovnik/lia/"
type: "slovnik"
title: "LIA – Location Information Answer"
date: 2025-01-01
abbr: "LIA"
fullName: "Location Information Answer"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/lia/"
summary: "Standardizovaná odpovědní zpráva v rámci architektury lokalizačních služeb (LCS) 3GPP. Je odeslána lokalizačním serverem (např. GMLC) žádajícímu klientovi (např. LCS klientovi) za účelem doručení poža"
---

LIA (Location Information Answer) je standardizovaná odpovědní zpráva odeslaná lokalizačním serverem žádajícímu klientovi za účelem doručení požadovaných lokalizačních informací o cílovém uživatelském zařízení v rámci architektury lokalizačních služeb 3GPP.

## Popis

Zpráva Location Information Answer (LIA) je klíčová zpráva na aplikační úrovni protokolu Diameter definovaná v rámci architektury [LCS](/mobilnisite/slovnik/lcs/) 3GPP. Funguje jako konečná odpověď na Location Information Request ([LIR](/mobilnisite/slovnik/lir/)). Primární funkcí LIA je předat geografickou polohu, rychlost a přidruženou přesnost cílového UE, které byly určeny síťovými lokalizačními mechanismy. Zpráva je přenášena protokolem Diameter, typicky na rozhraní SLg mezi Evolved Serving Mobile Location Center ([E-SMLC](/mobilnisite/slovnik/e-smlc/)) a Gateway Mobile Location Center ([GMLC](/mobilnisite/slovnik/gmlc/)), nebo na rozhraní Le pro přístup externích aplikací.

Zpráva LIA obsahuje bohatou sadu atribut-hodnotových párů ([AVP](/mobilnisite/slovnik/avp/)), které zapouzdřují výsledek lokalizace. Mezi klíčové AVP patří User-Location-Info, který poskytuje skutečné souřadnice (např. zeměpisná šířka, délka, nadmořská výška), a Accuracy-Fulfilment-Indicator, který specifikuje, zda byla dosažena požadovaná úroveň přesnosti. Další důležité AVP mohou indikovat použitou lokalizační metodu (např. [A-GNSS](/mobilnisite/slovnik/a-gnss/), [OTDOA](/mobilnisite/slovnik/otdoa/), [E-CID](/mobilnisite/slovnik/e-cid/)), stáří lokalizačního odhadu a rychlost UE, pokud je dostupná. Struktura zajišťuje interoperabilitu mezi různými síťovými elementy a externími LCS klienty.

V rámci LCS procedury funguje GMLC jako centrální uzel. Po přijetí LIR od autorizovaného klienta provede GMLC autorizaci účastníka a ověření ochrany soukromí. Poté přepošle požadavek příslušnému Mobility Management Entity (MME) a následně E-SMLC. E-SMLC řídí lokalizační relaci s UE a/nebo s rádiovou přístupovou sítí (např. eNodeB). Jakmile je poloha vypočtena, odešle E-SMLC odhad polohy zpět řetězcem a GMLC sestaví konečnou zprávu LIA pro žádajícího klienta. Tento komplexní proces, zakončený doručením LIA, je zásadní pro služby jako E911, sledování vozového parku a lokalizačně založené účtování.

## K čemu slouží

LIA byla zavedena za účelem standardizace poskytování lokalizačních informací v sítích 3GPP, čímž nahradila proprietární a roztříštěné metody. Před její standardizací bylo poskytování polohy UE externím aplikacím nebo pro regulatorní služby (jako nouzová volání) složité a závislé na dodavateli, což bránilo interoperabilitě a rozvoji robustního ekosystému pro lokalizačně založené služby (LBS). LIA jako součást architektury LCS založené na protokolu Diameter vytváří jasný, bezpečný a spolehlivý model žádost-odpověď.

Její vytvoření bylo primárně motivováno regulatorními požadavky, jako je Enhanced 911 (E911) ve Spojených státech a evropské nouzové číslo 112, které vyžadují, aby mobilní sítě poskytovaly přesnou polohu volajícího místům příjmu tísňových volání (PSAP). Dále komerční potenciál LBS pro navigaci, sociální sítě a cílenou reklamu vyžadoval škálovatelné a standardizované rozhraní. LIA řeší problém, jak spolehlivě a bezpečně vrátit vypočítanou polohu z interních lokalizačních systémů sítě autorizované externí entitě, se správným zacházením s ochranou soukromí a souhlasem uživatele podle specifikací 3GPP.

## Klíčové vlastnosti

- Standardizovaná zpráva protokolu Diameter pro interoperabilní doručení lokalizace
- Nese přesné souřadnice UE (zeměpisná šířka, délka, nadmořská výška) a data o přesnosti
- Podporuje zahrnutí informace o vektoru rychlosti pro pohybující se cíle
- Indikuje použitou lokalizační technologii (např. A-GNSS, OTDOA)
- Obsahuje časová razítka pro stáří a dobu platnosti lokalizace
- Zapouzdřuje výsledkové kódy indikující úspěch, selhání nebo zamítnutí autorizace

## Související pojmy

- [LCS – Location Services](/mobilnisite/slovnik/lcs/)
- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [E-SMLC – Enhanced Serving Mobile Location Centre](/mobilnisite/slovnik/e-smlc/)
- [LIR – Location Information Request](/mobilnisite/slovnik/lir/)

## Definující specifikace

- **TS 23.380** (Rel-19) — IMS Restoration Procedures
- **TR 29.949** (Rel-19) — VoLTE IMS Roaming Architecture & Procedures

---

📖 **Anglický originál a plná specifikace:** [LIA na 3GPP Explorer](https://3gpp-explorer.com/glossary/lia/)
