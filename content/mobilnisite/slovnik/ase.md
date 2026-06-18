---
slug: "ase"
url: "/mobilnisite/slovnik/ase/"
type: "slovnik"
title: "ASE – Application Service Element"
date: 2025-01-01
abbr: "ASE"
fullName: "Application Service Element"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ase/"
summary: "ASE je standardizovaná komponenta v architektuře 3GPP CAMEL, která poskytuje služby inteligentní sítě pro mobilní účastníky. Umožňuje operátorům nabízet nadstandardní služby, jako je předplacené účtov"
---

ASE je standardizovaná komponenta v architektuře 3GPP CAMEL, která poskytuje služby inteligentní sítě, jako je například předplacené účtování, prostřednictvím interakce s jádrem sítě během zpracování hovoru.

## Popis

Application Service Element (ASE) je základní stavební prvek v architektuře 3GPP Customised Applications for Mobile network Enhanced Logic ([CAMEL](/mobilnisite/slovnik/camel/)), definovaný jako součást frameworku Intelligent Network ([IN](/mobilnisite/slovnik/in/)) pro mobilní sítě. ASE funguje jako komponenta aplikační logiky, která sídlí ve funkci Service Control Function ([SCF](/mobilnisite/slovnik/scf/)) nebo na aplikačním serveru ([AS](/mobilnisite/slovnik/as/)) a implementuje konkrétní služební schopnosti prostřednictvím standardizovaných rozhraní s jádrem sítě. Když účastník zahájí nebo přijme hovor či datovou session, funkce Service Switching Function ([SSF](/mobilnisite/slovnik/ssf/)) v jádru sítě detekuje spouštěcí podmínky a pozastaví zpracování hovoru, aby se dotázala ASE na pokyny, jak pokračovat, což umožňuje řízení služeb v reálném čase.

Architektonicky ASE komunikuje s jádrem sítě pomocí protokolu CAMEL Application Part ([CAP](/mobilnisite/slovnik/cap/)) nad frameworkem [INAP](/mobilnisite/slovnik/inap/) (Intelligent Network Application Part). ASE obsahuje programy aplikační logiky ([SLP](/mobilnisite/slovnik/slp/)), které se spouštějí na základě profilů účastníků, síťových událostí a dat specifických pro službu. Mezi klíčové komponenty patří prostředí pro vykonávání aplikační logiky (SLEE), které hostí programy ASE, funkce Service Data Function (SDF) pro ukládání dat účastníků a služeb a specializované funkce pro zpracování médií, je-li to potřeba. ASE komunikuje s více síťovými elementy včetně Mobile Switching Center (MSC), Serving GPRS Support Node (SGSN) a Gateway MSC (GMSC) prostřednictvím standardizovaných referenčních bodů.

Během provozu ASE přijímá od SSF tzv. Initial Detection Points (IDP), když v síti nastanou předdefinované spouštěcí podmínky. ASE pak tyto události zpracuje pomocí své aplikační logiky, což může zahrnovat dotazování na databáze účastníků, provádění kontrol kreditu, úpravu směrování hovoru nebo zahájení dalších síťových interakcí. ASE odpovídá pomocí CAP operací, jako jsou Continue, Connect, ReleaseCall nebo RequestReportBCSMEvent, aby řídila tok hovoru. Pro pokročilé služby může ASE navázat dialog se specializovanými funkcemi pro hlášení, generování tónů nebo interakci s uživatelem prostřednictvím in-band signalizace.

V širší síťové architektuře ASE umožňuje oddělení aplikační logiky od základních přepínacích funkcí, což operátorům dovoluje vyvíjet a nasazovat služby nezávisle na dodavateli jejich jádra sítě. Tento modulární přístup podporuje služby jako předplacené účtování, kde ASE monitoruje délku hovoru a odečítá kredit v reálném čase, virtuální privátní sítě, kde ASE upravuje volaná čísla na základě firemních číslovacích plánů, a služby založené na poloze, kde ASE dotazuje na polohu účastníka a podle toho aplikuje aplikační logiku. Standardizované rozhraní ASE zajišťuje interoperabilitu mezi různými dodavateli síťového vybavení a umožňuje vývojářům služeb třetích stran vytvářet aplikace fungující napříč sítěmi více operátorů.

## K čemu slouží

ASE byla vytvořena, aby řešila omezení tradičních mobilních sítí, kde byla aplikační logika pevně svázána s přepínacím zařízením, což činilo nasazení služeb pomalým, nákladným a závislým na dodavateli. Před zavedením CAMEL a ASE museli operátoři čekat, až jejich dodavatelé ústředen vyvinou a implementují nové služby, což vedlo k dlouhé době uvedení na trh a omezené inovaci služeb. Koncept Intelligent Network, jehož je ASE klíčovou součástí, zavedl standardizovaný způsob oddělení aplikační logiky od základního zpracování hovoru, což operátorům umožnilo vyvíjet služby nezávisle a nasazovat je napříč sítěmi více dodavatelů.

Primární problém, který ASE řeší, je potřeba reálného, inteligentního řízení mobilních služeb bez nutnosti úprav jádrových síťových ústředen. Tradiční přístupy vyžadovaly aktualizaci softwaru ústředny pro každou novou službu, což bylo časově náročné a ohrožovalo stabilitu sítě. ASE umožňuje služby jako předplacené účtování, které vyžaduje monitorování kreditu a řízení hovoru v reálném čase – funkcionalitu, kterou základní ústředny nebyly navrženy poskytovat. Standardizací rozhraní mezi aplikační logikou a síťovými ústřednami ASE umožňuje operátorům rychle zavádět nové služby generující příjmy při zachování spolehlivosti sítě.

Historicky se vývoj ASE v 3GPP Release 5 časově shodoval s růstem mobilních datových služeb a potřebou sofistikovanějšího řízení služeb nad rámec základních hlasových hovorů. Řešil omezení dřívějších implementací IN, které byly navrženy primárně pro pevné sítě a nezohledňovaly požadavky specifické pro mobilní komunikaci, jako je mobilita účastníka, roaming a povědomí o poloze. ASE poskytla optimalizovaný framework pro mobilní sítě, který dokázal zvládnout komplexnost sítí GSM a UMTS při zachování zpětné kompatibility se stávajícími standardy IN, což zajistilo hladkou migrační cestu pro operátory investující do schopností inteligentní sítě.

## Klíčové vlastnosti

- Standardizované CAMEL rozhraní pro interoperabilitu více dodavatelů
- Řízení hovoru/session v reálném čase prostřednictvím CAP protokolových operací
- Oddělení aplikační logiky od přepínacích funkcí jádra sítě
- Podpora předplaceného účtování s řízením kreditu v reálném čase
- Služby Virtual Private Network (VPN) s firemními číslovacími plány
- Spouštění a řízení služeb založených na poloze

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 29.013** (Rel-19) — MAP-SSAP Interworking for CCBS Service
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- **TS 29.458** (Rel-8) — SIP Transfer of Tariff Info for Charging
- **TS 29.658** (Rel-19) — SIP Transfer of Tariff Information
- **TS 33.108** (Rel-19) — LI Handover Interface Specification

---

📖 **Anglický originál a plná specifikace:** [ASE na 3GPP Explorer](https://3gpp-explorer.com/glossary/ase/)
