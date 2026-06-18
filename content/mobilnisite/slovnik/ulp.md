---
slug: "ulp"
url: "/mobilnisite/slovnik/ulp/"
type: "slovnik"
title: "ULP – User Plane Location Protocol"
date: 2025-01-01
abbr: "ULP"
fullName: "User Plane Location Protocol"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ulp/"
summary: "ULP je protokol definovaný organizacemi 3GPP a OMA pro doručování polohových informací po uživatelské rovině. Umožňuje polohové služby, jako jsou tísňová volání, navigace a služby založené na poloze,"
---

ULP je protokol 3GPP a OMA pro doručování polohových informací po uživatelské rovině, který umožňuje polohové služby přenosem zpráv mezi zařízením a polohovým serverem.

## Popis

User Plane Location Protocol (ULP) je protokol typu klient-server standardizovaný společně organizací 3GPP a Open Mobile Alliance ([OMA](/mobilnisite/slovnik/oma/)). Funguje přes IP připojení na uživatelské rovině, typicky využívající [HTTP](/mobilnisite/slovnik/http/)/[HTTPS](/mobilnisite/slovnik/https/) nebo [SUPL](/mobilnisite/slovnik/supl/) jako transportní vrstvu, a usnadňuje výměnu polohových informací mezi Secure User Plane Location (SUPL) Enabled Terminal ([SET](/mobilnisite/slovnik/set/)) – což je typicky User Equipment (UE) – a SUPL Location Platform ([SLP](/mobilnisite/slovnik/slp/)). Protokol přenáší zprávy pro polohové procedury, včetně výměny schopností, vyjednávání polohové metody a doručování asistenčních dat nebo polohových měření a výsledků.

Z architektonického hlediska jsou ULP zprávy zapouzdřeny v rámci SUPL relací. SLP může vystupovat ve dvou hlavních rolích: jako SUPL Location Center ([SLC](/mobilnisite/slovnik/slc/)), které spravuje relace, ochranu soukromí a doručování asistenčních dat, a jako SUPL Positioning Center ([SPC](/mobilnisite/slovnik/spc/)), které provádí výpočet polohy. SET (UE) obsahuje SUPL Agent, což je aplikace žádající o polohu, a polohový engine. ULP definuje komplexní sadu typů zpráv, včetně SUPL START, SUPL RESPONSE, SUPL POS INIT a SUPL END, které řídí celou polohovou relaci.

Jak funguje: sekvence výměny zpráv. Požadavek na polohu spustí SUPL Agent na SET, který zahájí ULP relaci odesláním zprávy SUPL START na SLP. Tato zpráva obsahuje schopnosti SET a požadovanou kvalitu služby (QoS). SLP odpoví zprávou SUPL RESPONSE, která označuje zvolenou polohovou metodu (např. A-GNSS, OTDOA, E-CID). Následně je navázána SUPL POS relace, kde SET a SLP vyměňují polohově specifické zprávy (pomocí protokolů RRLP, RRC nebo LPP/LLP) za účelem přenosu asistenčních dat, měřicích dat a nakonec vypočteného odhadu polohy. Relace je ukončena zprávou SUPL END.

Jeho role v síti je klíčová pro komerční i regulované polohové služby. Využitím uživatelské roviny se obejde potřeba integrace do signalizační roviny jádra sítě pro každou polohovou technologii, což nabízí větší flexibilitu a rychlejší nasazení nových polohových funkcí. Podporuje více polohových technologií, síťově iniciované i mobilním zařízením iniciované požadavky na polohu a je základním kamenem pro tísňové služby jako E911 a E112, stejně jako pro komerční aplikace jako navigace a sledování majetku.

## K čemu slouží

ULP byl vytvořen, aby poskytl standardizovaný, IP-based protokol pro poskytování polohových služeb po uživatelské rovině, čímž řeší omezení metod určování polohy na řídicí rovině. Před ULP se polohové služby primárně spoléhaly na signalizaci v řídicí rovině uvnitř jádra sítě s přepojováním okruhů nebo paketů (např. využitím RRLP přes rádiové rozhraní GSM/UMTS). Tento přístup byl těsně svázán se specifickými síťovými architekturami, což ztěžovalo nasazování nových polohových metod a služeb napříč různými operátorskými sítěmi a typy zařízení. Metody na řídicí rovině také mohly zatěžovat jádro sítě významnou signalizační zátěží.

Motivace pro ULP, vyvinutý v rámci standardu OMA SUPL a přijatý 3GPP, byla využít všudypřítomné IP konektivity datových sítí. Přesunutím polohové signalizace na uživatelskou rovinu odděluje polohové služby od podkladové technologie rádiového přístupu a jádra sítě. To umožňuje rychlejší inovace a nasazení pokročilých polohových technik (jako A-GNSS a OTDOA) a služeb. Zjednodušuje interoperabilitu mezi koncovými zařízeními a polohovými servery od různých výrobců.

Dále ULP řeší problém umožnění vysoce přesných, nízkolatenčních polohových služeb pro tísňová volání a komerční aplikace bez přetěžování starší infrastruktury s přepojováním okruhů. Poskytuje bezpečný, škálovatelný rámec (pomocí HTTPS), který podporuje ochranu soukromí, scénáře roamingu a širokou škálu polohových protokolů, čímž se stal de facto standardem pro síťově asistovaný GPS a hybridní určování polohy v moderních mobilních sítích.

## Klíčové vlastnosti

- Funguje přes IP-based uživatelskou rovinu (např. HTTPS) pro flexibilní nasazení
- Podporuje více polohových protokolů (RRLP, RRC, LPP/LLP) uvnitř svých zpráv
- Umožňuje jak mobilním zařízením iniciované, tak síťově iniciované požadavky na polohu
- Poskytuje zabezpečení pomocí šifrování TLS/SSL a autentizačních mechanismů
- Obsahuje komplexní procedury správy relací a vyjednávání schopností
- Usnadňuje doručování asistenčních dat (např. GPS efemerid) do zařízení

## Související pojmy

- [SUPL – Secure User Plane for Location](/mobilnisite/slovnik/supl/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [A-GNSS – Assisted Global Navigation Satellite Systems](/mobilnisite/slovnik/a-gnss/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [SLP – Service Location Protocol](/mobilnisite/slovnik/slp/)

## Definující specifikace

- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)

---

📖 **Anglický originál a plná specifikace:** [ULP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ulp/)
