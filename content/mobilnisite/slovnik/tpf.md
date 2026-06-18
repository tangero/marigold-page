---
slug: "tpf"
url: "/mobilnisite/slovnik/tpf/"
type: "slovnik"
title: "TPF – Traffic Plane Function"
date: 2025-01-01
abbr: "TPF"
fullName: "Traffic Plane Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tpf/"
summary: "Funkce provozní roviny (TPF) je síťový prvek zodpovědný za vynucování pravidel pro politiku a účtování na uživatelském datovém provozu v reálném čase. Spolupracuje s funkcí pravidel pro politiku a účt"
---

TPF je síťový prvek, který v reálném čase vynucuje pravidla pro politiku a účtování na uživatelském datovém provozu aplikací akcí, jako je řízení přístupu (gating), filtrování a stanovování priority.

## Popis

Funkce provozní roviny (TPF) je klíčová komponenta v architektuře řízení politiky a účtování ([PCC](/mobilnisite/slovnik/pcc/)) dle 3GPP, konkrétně definovaná v kontextu systému účtování na základě toku ([FBC](/mobilnisite/slovnik/fbc/)). Je to entita, která se nachází v cestě uživatelských dat (v provozní rovině) a je zodpovědná za detekci, zpracování a akci na toky služebních dat v reálném čase na základě pokynů od funkce pravidel pro politiku a účtování ([PCRF](/mobilnisite/slovnik/pcrf/)). V mnoha implementacích je TPF integrována do uzlu brány, jako je Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) v EPC nebo User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) v 5GC.

Architektonicky se TPF skládá z několika klíčových podfunkcí: funkce detekce toku služebních dat, která identifikuje pakety patřící do konkrétního toku pomocí filtrů (např. na základě 5-tice); funkce vynucování politiky, která aplikuje akce jako řízení přístupu (povolení/blokování), řízení šířky pásma a označování QoS; a funkce účtování, která provádí měření využití a komunikuje s online a offline systémy účtování. TPF komunikuje s PCRF přes referenční bod Gx, přijímá pravidla řízení politiky a účtování (PCC), která definují zacházení s každým detekovaným tokem. Tato pravidla zahrnují parametry pro QoS ([QCI](/mobilnisite/slovnik/qci/), [ARP](/mobilnisite/slovnik/arp/)), účtovací klíče a použité metody účtování.

Jak to funguje, zahrnuje kontinuální cyklus. Když uživatel naváže datovou relaci, PCRF zřídí počáteční PCC pravidla pro TPF. Jak uživatelský provoz prochází bránou, TPF kontroluje pakety, přiřazuje je k aktivním šablonám toků služebních dat a aplikuje odpovídající akce politiky. Také měří objem provozu nebo dobu trvání pro účely účtování. Pokud událost vyvolá změnu politiky (např. uživateli dojde kvóta), může PCRF v reálném čase zaslat aktualizovaná pravidla do TPF. Role TPF je tedy být vynucovacím bodem, který překládá politiky služeb na vysoké úrovni do konkrétních akcí na úrovni paketů, což umožňuje diferencované služby, spravedlivé využití zdrojů a sofistikované modely účtování, jako je sponzorované připojení nebo zero-rating.

## K čemu slouží

TPF byla vytvořena, aby řešila potřebu dynamického řízení politiky a účtování na základě toku v IP mobilních sítích. Dřívější systémy před IMS měly statickou QoS založenou na předplatném a jednoduché objemové účtování, což bylo nedostatečné pro nabízení služeb v různých úrovních, politiky specifické pro aplikace a kontroly utrácení v reálném čase. TPF jako součást rámce [PCC](/mobilnisite/slovnik/pcc/) zavedla oddělení mezi řídicí rovinou (PCRF), která činí rozhodnutí o politice, a uživatelskou rovinou, která je vynucuje.

Problémy, které řeší, zahrnují neschopnost aplikovat různé politiky na různé typy provozu od stejného uživatele (např. upřednostňování VoIP před prohlížením webu) a nedostatek integrace mezi účtováním a vynucováním politiky. Nasazením TPF do cesty provozu získali operátoři schopnost vytvářet a zpoplatňovat nové nabídky služeb, inteligentněji řídit zahlcení sítě a poskytovat účastníkům oznámení a kontroly nad jejich datovým využitím v reálném čase. Její zavedení ve vydání 6 bylo motivováno růstem datových služeb a požadavkem na mechanismus účtování a politiky kompatibilní s IMS, který by mohl podporovat složité scénáře služeb.

## Klíčové vlastnosti

- Detekce toků služebních dat v reálném čase pomocí konfigurovatelných paketových filtrů
- Vynucování akcí řízení přístupu (povolit/zakázat), označování QoS a řízení šířky pásma
- Integrace řízení politiky s funkcemi online a offline účtování
- Komunikace s PCRF přes rozhraní Gx pro dynamické zřizování pravidel
- Podpora správy provozu s ohledem na aplikace a sponzorovaného připojení
- Často umístěna společně s funkcemi brány (GGSN, PGW, UPF) v uživatelské rovině

## Související pojmy

- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [PCC – Performance-oriented Congestion Control](/mobilnisite/slovnik/pcc/)

## Definující specifikace

- **TS 23.125** (Rel-7) — Flow Based Charging Architecture
- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.246** (Rel-19) — MBMS Bearer Service Stage 2 Description
- **TS 23.803** (Rel-7) — PCC Architecture Harmonization Study
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.278** (Rel-19) — Monitoring Events Offline Charging Specification

---

📖 **Anglický originál a plná specifikace:** [TPF na 3GPP Explorer](https://3gpp-explorer.com/glossary/tpf/)
