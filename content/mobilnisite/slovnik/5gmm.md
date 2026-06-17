---
slug: "5gmm"
url: "/mobilnisite/slovnik/5gmm/"
type: "slovnik"
title: "5GMM – 5G Mobility Management"
date: 2025-01-01
abbr: "5GMM"
fullName: "5G Mobility Management"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/5gmm/"
summary: "5GMM je řídicí protokol v 5G, který spravuje stavy mobility a registrace UE (uživatelského zařízení) v 5G Core síti. Zpracovává procedury jako registrace, odregistrování a servisní požadavky, což umož"
---

5GMM je řídicí protokol 5G, který spravuje mobilitu, registraci a připojení UE (uživatelského zařízení) za účelem umožnění přístupu k síti a kontinuity služeb.

## Popis

Protokol 5G Mobility Management (5GMM) je protokol ne-přístupové vrstvy (NAS) definovaný ve specifikacích 3GPP, především v TS 24.501. Funguje mezi uživatelským zařízením (UE) a funkcí pro správu přístupu a mobility (AMF) v 5G Core síti (5GC). 5GMM je zodpovědný za správu mobility a registračního kontextu UE, zajišťuje, aby mohlo bezpečně a efektivně přistupovat k síťovým službám. Vytváří a udržuje signalizační spojení NAS, které je klíčové pro veškerou řídicí komunikaci mezi UE a jádrem sítě, nezávisle na podkladové technologii rádiového přístupu (např. NG-RAN, ne-3GPP přístup).

5GMM funguje na základě specifických stavů, které definují registrační stav UE v síti. Dva hlavní stavy jsou 5GMM-REGISTERED a 5GMM-DEREGISTERED. Ve stavu REGISTERED úspěšně provedlo UE registraci u AMF a je navázáno signalizační spojení NAS, což umožňuje UE iniciovat servisní požadavky, přijímat paging a udržovat svůj mobilní kontext. Ve stavu DEREGISTERED není UE registrováno a síť pro něj neuchovává kontext, i když UE může stále provádět počáteční registrační procedury. 5GMM také spravuje podstavy jako 5GMM-IDLE a 5GMM-CONNECTED, které odrážejí stav konektivity signalizačního spoje NAS.

Klíčové procedury řízené 5GMM zahrnují počáteční registraci, periodickou aktualizaci registrace, aktualizaci registrace při mobilitě (např. když se UE přesune do nové sledovací oblasti), odregistrování (iniciované UE nebo sítí) a servisní požadavek. Procedura servisního požadavku je klíčová, neboť převádí UE ze stavu 5GMM-IDLE do 5GMM-CONNECTED za účelem vytvoření prostředků uživatelské roviny pro přenos dat. 5GMM také zajišťuje autentizaci a zabezpečení interakcí s funkcí autentizačního serveru (AUSF) a funkcí bezpečnostní kotvy (SEAF), aby zajistil bezpečnou signalizaci NAS, včetně ochrany integrity a šifrování zpráv NAS.

5GMM je úzce integrován s dalšími funkcemi 5G jádra sítě. Spolupracuje s funkcí pro správu relací (SMF) prostřednictvím AMF při správě PDU (Protocol Data Unit) relací. Zatímco 5GMM řeší mobilitu a registraci, parametry specifické pro relaci spravuje protokol 5G Session Management (5GSM). Toto oddělení umožňuje flexibilnější a škálovatelnější síťové architektury, podporující funkce jako síťové segmenty (network slicing) a edge computing. 5GMM také podporuje pokročilé mobilní scénáře, včetně předávání mezi 3GPP a ne-3GPP přístupovými sítěmi a spolupráce s EPS (Evolved Packet System) pro scénáře přechodu (fallback).

## K čemu slouží

5GMM byl vytvořen jako součást architektury 5G systému, aby řešil omezení protokolu Evolved Packet System (EPS) Mobility Management (EMM) používaného v 4G LTE. Se zavedením 5G vznikla potřeba flexibilnějšího, škálovatelnějšího a efektivnějšího protokolu pro správu mobility, který by podporoval rozmanité případy užití, včetně rozšířeného mobilního širokopásmového připojení (eMBB), ultra-spolehlivých nízkolatenčních komunikací (URLLC) a komunikací hromadného typu stroj-stroj (mMTC). EMM, ač efektivní pro 4G, nebyl navržen pro zvládnutí zvýšené složitosti, síťových segmentů a integrace heterogenních přístupů vyžadovaných pro 5G.

Hlavní problémy, které 5GMM řeší, zahrnují zjednodušení signalizačních procedur ke snížení latence, podporu bezproblémové mobility napříč více typy přístupu (např. 3GPP NG-RAN, Wi-Fi, pevné sítě) a umožnění efektivního využití síťových zdrojů. Zavádí architekturu založenou na službách (SBA) v jádru sítě, kde AMF funguje jako jediný vstupní bod pro signalizaci NAS, odděluje správu mobility od správy relací. Toto oddělení umožňuje nezávislé škálování a optimalizaci funkcí, což je klíčové pro nasazení síťových segmentů šitých na míru specifickým požadavkům služeb.

Historicky byla správa mobility v předchozích generacích (např. 4G EMM) těsně provázána se správou relací, což vedlo k menší flexibilitě. 5GMM to řeší definováním jasných stavových modelů a procedur, které snižují signalizační režii a zlepšují energetickou účinnost zařízení, zejména IoT senzorů. Také posiluje zabezpečení začleněním nových autentizačních rámců a podporou souběžných více registrací pro různé síťové segmenty. Vytvoření 5GMM bylo motivováno potřebou podporovat širší škálu scénářů nasazení, od hustých městských oblastí po průmyslový IoT, při zachování zpětné kompatibility a spolupráce se sítěmi 4G prostřednictvím procedur jako předávání a přechod (fallback).

## Klíčové vlastnosti

- Spravuje procedury registrace a odregistrování UE v 5G jádru sítě
- Řídí přechody mezi stavy mobility (např. z 5GMM-IDLE do 5GMM-CONNECTED) pro efektivní využití zdrojů
- Podporuje procedury servisních požadavků pro navázání konektivity uživatelské roviny pro datové relace
- Integruje se s autentizačními a bezpečnostními mechanismy pro zabezpečenou signalizaci NAS
- Umožňuje mobilitu mezi 3GPP a ne-3GPP přístupovými sítěmi
- Usnadňuje síťové segmenty (network slicing) správou registračních kontextů pro různé segmenty

## Definující specifikace

- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3
- **TS 29.214** (Rel-19) — Policy and Charging Control over Rx
- **TS 38.508** (Rel-19) — 5G NR UE Radio Transmission & Reception

---

📖 **Anglický originál a plná specifikace:** [5GMM na 3GPP Explorer](https://3gpp-explorer.com/glossary/5gmm/)
