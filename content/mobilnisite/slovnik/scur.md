---
slug: "scur"
url: "/mobilnisite/slovnik/scur/"
type: "slovnik"
title: "SCUR – Session Charging with Unit Reservation"
date: 2025-01-01
abbr: "SCUR"
fullName: "Session Charging with Unit Reservation"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/scur/"
summary: "SCUR je metoda systému online účtování (OCS), při které síť rezervuje účtovací jednotky (např. peníze, objem dat, čas) před povolením využití služby. Zajišťuje řízení kreditu v reálném čase, čímž zabr"
---

SCUR je metoda online účtování, při které síť v reálném čase rezervuje jednotky (např. peněžní částku, objem dat) před povolením využití služby, což umožňuje předplacené služby a zabraňuje překročení kreditu.

## Popis

Session Charging with Unit Reservation (SCUR) je klíčová funkce v rámci 3GPP Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)), podrobně popsaná ve specifikacích jako TS 32.240 a TS 32.251. Funguje na principu rezervace kreditu před spotřebou služby, což umožňuje online účtování pro předplacené a služby na vyžádání. Architektura zahrnuje několik klíčových síťových funkcí: Charging Trigger Function ([CTF](/mobilnisite/slovnik/ctf/)) integrovanou v síťových prvcích jako GGSN, [P-GW](/mobilnisite/slovnik/p-gw/) nebo [S-CSCF](/mobilnisite/slovnik/s-cscf/), která detekuje účtovatelné události; Online Charging Function ([OCF](/mobilnisite/slovnik/ocf/)) v rámci OCS, která spravuje řízení kreditu; a Account Balance Management Function ([ABMF](/mobilnisite/slovnik/abmf/)), která uchovává zůstatky na účtech účastníků. Když uživatel zahájí servisní relaci (např. datovou relaci, hovor nebo službu zasílání zpráv), CTF odešle požadavek na řízení kreditu (credit control request) k OCF. OCF následně komunikuje s ABMF, aby ověřila zůstatek účastníka, a pokud je dostatečný, rezervuje pro danou relaci určitý počet jednotek (peněžních, objemu dat nebo časových). Tato rezervace je přidělena CTF, což umožní pokračování služby. Jak je služba spotřebovávána, CTF hlásí OCF využit jednotky, které OCF odečte z rezervace a následně ze zůstatku na účtu. Pokud je rezervace vyčerpána, OCF může přidělit další jednotky (opětovná autorizace) nebo ukončit relaci, pokud není dostatečný zůstatek.

Proces SCUR se řídí protokolem Diameter Credit-Control Application ([DCCA](/mobilnisite/slovnik/dcca/)), jak je definováno v [RFC](/mobilnisite/slovnik/rfc/) 4006 a přijato 3GPP. Tento protokol usnadňuje výměnu zpráv řízení kreditu mezi CTF a OCF. Mezi klíčové typy zpráv patří Credit-Control-Request (CCR) a Credit-Control-Answer (CCA). OCF využívá ratingové funkce pro převod parametrů využití služby na peněžní nebo jednotkové náklady na základě tarifních informací. SCUR podporuje více modelů rezervace: rezervaci částky (rezervace konkrétního množství jednotek), správu kvót (dynamické upravování rezervace) a sdílenou kvótu (pooled-quota, sdílení kvóty napříč více relacemi). Tato flexibilita umožňuje pokrýt různé typy služeb, od jednoduchých hovorů po složité multimediální relace založené na IMS.

Role SCUR v síti je klíčová pro zajištění příjmů a řízení služeb. Umožňuje operátorům nabízet předplacené služby bez rizika špatných pohledávek, protože využití je striktně omezeno na dostupný kredit. Dále podporuje pokročilé scénáře účtování, jako je rozdělené účtování (kdy je účtováno více stranám), účtování na základě polohy a služebně specifické tarify. Integrací s řízením politik (prostřednictvím PCRF) může SCUR také ovlivňovat kvalitu služeb (QoS) na základě rozhodnutí o účtování, čímž vytváří soudržnou řídicí rovinu pro zpoplatnění a správu zdrojů. Její implementace je povinná pro síťové prvky podporující online účtování, což z ní činí všudypřítomnou součást moderních 3GPP sítí.

## K čemu slouží

SCUR byl vyvinut k řešení základního obchodního požadavku na online, předplacené účtování v telekomunikačních sítích. Před systémy online účtování dominovalo účtování ex post (postpaid), kdy se využití zaznamenalo a fakturovalo dodatečně, což pro operátory představovalo úvěrové riziko. Vzestup předplacených mobilních služeb vyžadoval mechanismus pro řízení využití služeb v reálném čase na základě dostupného kreditu, aby účastníci nepřekročili své zůstatky. SCUR tuto schopnost poskytl zavedením modelu založeného na rezervaci, který zajišťuje, že síťové zdroje jsou spotřebovávány až po zajištění platební garance. Tím byla vyřešena problematika úniku příjmů a umožněno masové globální rozšíření předplacených mobilních tarifů.

Motivace pro SCUR vycházela z omezení offline účtování (účtování po události) a jednoduchých předplacených řešení, která byla často závislá na dodavateli a postrádala interoperabilitu. Jak se sítě vyvíjely a nabízely rozmanité služby (GPRS, IMS, MMS), se stala nezbytnou standardizovaná a flexibilní metoda online účtování. 3GPP zavedlo SCUR jako součást širší architektury Charging and Billing (CAB) za účelem vytvoření jednotného rámce. Řešilo potřebu granulárního účtování na úrovni relace, podpory více typů služeb a integrace se síťovými politikami. To umožnilo operátorům uvádět inovativní tarifní plány, jako jsou balíčky dat na bázi objemu, časově omezené nabídky a účtování na základě obsahu, čímž se zvýšila konkurenceschopnost a spokojenost zákazníků.

Historicky SCUR umožnil konvergenci účtování napříč okruhově přepínanou, paketově přepínanou a IMS doménou. Poskytl budoucím službám, jako je VoLTE, připojení IoT nebo síťové segmentace (network slicing), odolný základ pro účtování. Standardizací interakce mezi síťovými prvky a OCS snížil SCUR provozní složitost a usnadnil nasazení od více dodavatelů. Jeho vytvoření bylo hnací silou komerčního imperativu spolehlivě a flexibilně zpoplatňovat síťové služby v rostoucí digitální a ekonomice na vyžádání.

## Klíčové vlastnosti

- Rezervace kreditu v reálném čase před autorizací služby
- Integrace s protokolem Diameter Credit-Control Application (DCCA)
- Podpora více typů jednotek: peněžní, objem dat, čas
- Dynamická správa kvót a opětovná autorizace během relací
- Interakce s funkcí správy zůstatků na účtu (Account Balance Management Function – ABMF)
- Umožňuje předplacené služby a zabraňuje překročení kreditu

## Definující specifikace

- **TS 28.203** (Rel-18) — Charging management
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.260** (Rel-19) — IMS Charging Management
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.273** (Rel-19) — MBMS Charging Management
- **TS 32.277** (Rel-19) — Charging Management for Proximity Services (ProSe)
- **TS 32.278** (Rel-19) — Monitoring Events Offline Charging Specification
- **TS 32.280** (Rel-19) — Advice of Charge (AoC) Framework

---

📖 **Anglický originál a plná specifikace:** [SCUR na 3GPP Explorer](https://3gpp-explorer.com/glossary/scur/)
