---
slug: "ecf"
url: "/mobilnisite/slovnik/ecf/"
type: "slovnik"
title: "ECF – Event Charging Function"
date: 2025-01-01
abbr: "ECF"
fullName: "Event Charging Function"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ecf/"
summary: "Event Charging Function (ECF) je klíčová komponenta 3GPP Online Charging Systemu (OCS). Zpracovává účtovací události v reálném čase, komunikuje s síťovými elementy a autorizuje využití služby na zákla"
---

ECF je komponenta Online Charging Systemu, která zpracovává účtovací události v reálném čase, aby na základě stavu účtu autorizovala využití služby, což umožňuje předplacené služby a okamžité strhávání poplatků.

## Popis

Event Charging Function (ECF) je základní logická entita v architektuře 3GPP Online Charging Systemu ([OCS](/mobilnisite/slovnik/ocs/)), jak je definována v sadě specifikací TS 32.2xx. Funguje v reálném čase a provádí okamžité rating a účtování za využití síťových zdrojů při výskytu služebních událostí. ECF je zodpovědná za zpracování 'účtovacích událostí' (charging events) vyvolaných síťovými funkcemi, jako jsou [MSC](/mobilnisite/slovnik/msc/), SGSN, GGSN, [P-CSCF](/mobilnisite/slovnik/p-cscf/) nebo [AS](/mobilnisite/slovnik/as/). Účtovací událost představuje diskrétní jednotku spotřeby služby, například uskutečnění hovoru, odeslání SMS, aktivaci datové relace nebo doručení staženého obsahu. Primární rolí ECF je určit peněžní nebo nepeněžní cenu takové události a autorizovat ji na základě zůstatku na uživatelském účtu v OCS.

ECF komunikuje s ostatními komponentami OCS přes standardizovaný referenční bod Ro (protokol Diameter). Když síťový element (fungující jako Charging Trigger Function, [CTF](/mobilnisite/slovnik/ctf/)) detekuje zpoplatnitelnou událost, odešle k ECF požadavek Credit Control Request ([CCR](/mobilnisite/slovnik/ccr/)). ECF následně spolupracuje s Account Balance Management Function ([ABMF](/mobilnisite/slovnik/abmf/)) pro kontrolu zůstatku účtu účastníka a s Rating Function (RF) pro určení ceny požadované služební jednotky. Na základě těchto informací ECF učiní autorizační rozhodnutí. Pokud je kredit dostupný, rezervuje odpovídající částku ze zůstatku a odpoví Credit Control Answer ([CCA](/mobilnisite/slovnik/cca/)) s přidělenou kvótou jednotek (např. vteřin hovoru, objemu dat v bajtech, počtu zpráv). Síťový element pak umožní pokračování služby a tuto kvótu spotřebovává. Po vyčerpání kvóty nebo ukončení služby je odeslán nový CCR a ECF strhne použitou částku z účtu a může přidělit novou kvótu. Tento proces zajišťuje kontrolu zůstatku v reálném čase.

Architektonicky lze ECF nasadit v různých modelech. V modelu 'Event-Based Charging' zpracovává okamžité diskrétní události, jako jsou SMS nebo MMS. Hraje také klíčovou roli v 'Session-Based Charging' prostřednictvím své integrace se Session Charging Function (SCF), kde může zpracovávat specifické události v rámci delší relace. ECF je ústřední pro umožnění předplacených služeb, kontrol výdajových limitů v reálném čase (např. pro datové balíčky) a konvergentního účtování, kde služby z více domén (hlas, data, zprávy) čerpají z jediného zůstatku. Její fungování je klíčové pro operátory, aby zabránili úniku příjmů, nabízeli flexibilní tarify a poskytovali účastníkům okamžitou zpětnou vazbu o spotřebě jejich kreditu.

## K čemu slouží

ECF byla vytvořena pro řešení základního obchodního požadavku na účtování v reálném čase (neboli 'online') a předplacené služby v mobilních sítích. Tradiční 'offline' účtování (založené na CDR) znamenalo zpoždění mezi využitím služby a vyúčtováním, což bylo nevhodné pro předplacené účastníky, kteří potřebují okamžité stržení zůstatku na účtu, aby nedocházelo k zadlužení. Před standardizovanou architekturou OCS dodavatelé implementovali proprietární předplacená řešení úzce propojená s konkrétními síťovými ústřednami, což omezovalo flexibilitu a interoperabilitu.

Standardizace ECF v rámci architektury 3GPP OCS, počínaje Release 5, tyto problémy vyřešila oddělením účtovací logiky od síťových elementů. Vytvořila jasné, otevřené rozhraní (Ro) pro všechny síťové funkce, aby žádaly o autorizaci kreditu jednotným způsobem. To umožnilo vytvoření centralizované platformy pro účtování v reálném čase, která může obsluhovat více služeb (okruhově přepínané, paketově přepínané, IMS) z jediného zůstatku účastníka. ECF umožnila operátorům zavádět sofistikované předplacené nabídky, implementovat kontrolu výdajů v reálném čase pro uživatele s fakturaci ex post a rychle uvádět nové služby se složitými událostními tarify. Byla klíčovým enablerem pro předplacený obchodní model, který globálně poháněl masové rozšíření mobilní komunikace, a zůstává nezbytná pro moderní konvergentní účtování.

## Klíčové vlastnosti

- Zpracovává účtovací události v reálném čase pro autorizaci služby
- Komunikuje s Rating Function (RF) pro určení tarifu
- Spolupracuje s Account Balance Management Function (ABMF) pro kontrolu a aktualizaci zůstatku
- Používá rozhraní Diameter Ro pro komunikaci se síťovými CTF
- Přiděluje a spravuje kvóty využití (čas, objem, události)
- Podporuje jak účtování založené na událostech (např. SMS), tak události v rámci účtování založeného na relacích

## Související pojmy

- [OCS – Originating Call Screening](/mobilnisite/slovnik/ocs/)
- [ABMF – Accounting Balance Management Function](/mobilnisite/slovnik/abmf/)

## Definující specifikace

- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.815** (Rel-5) — IMS Charging Implications
- **TR 23.979** (Rel-19) — PoC over 3GPP Systems Architectural Requirements
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 32.260** (Rel-19) — IMS Charging Management
- **TS 32.273** (Rel-19) — MBMS Charging Management

---

📖 **Anglický originál a plná specifikace:** [ECF na 3GPP Explorer](https://3gpp-explorer.com/glossary/ecf/)
