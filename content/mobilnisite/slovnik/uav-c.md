---
slug: "uav-c"
url: "/mobilnisite/slovnik/uav-c/"
type: "slovnik"
title: "UAV-C – Uncrewed Aerial Vehicle – Controller"
date: 2026-01-01
abbr: "UAV-C"
fullName: "Uncrewed Aerial Vehicle – Controller"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/uav-c/"
summary: "Služba 3GPP umožňující autorizovaným pozemním řídicím stanicím ovládat a spravovat bezpilotní letouny (UAV) prostřednictvím mobilních sítí. Poskytuje zabezpečené a spolehlivé spojení pro velení a říze"
---

UAV-C je služba 3GPP, která umožňuje autorizovaným pozemním řídicím stanicím ovládat a spravovat bezpilotní letouny prostřednictvím mobilních sítí pro zabezpečené operace BVLOS.

## Popis

Uncrewed Aerial Vehicle – Controller (UAV-C) je standardizovaná servisní architektura definovaná 3GPP pro usnadnění velení a řízení [UAV](/mobilnisite/slovnik/uav/), běžně známých jako drony, s využitím mobilních sítí 3GPP jako komunikačního spoje. Architektura zahrnuje několik klíčových síťových funkcí a rozhraní, aby zajistila zabezpečené, spolehlivé a nízkolatenční spojení mezi UAV-C (pozemním operátorem nebo automatizovaným systémem) a samotným UAV. Ke službě UAV-C se typicky přistupuje prostřednictvím UAV Service Supplier ([USS](/mobilnisite/slovnik/uss/)) nebo systému [UAS](/mobilnisite/slovnik/uas/) Traffic Management ([UTM](/mobilnisite/slovnik/utm/)), které komunikují se sítí 3GPP za účelem autentizace řídicí stanice, autorizace letu UAV a zřízení potřebných komunikačních cest.

Jádrem funkčnosti UAV-C je využití stávajících schopností základní sítě 3GPP, jako je Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)), Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) a Session Management Function ([SMF](/mobilnisite/slovnik/smf/)), které jsou rozšířeny o službě-specifická vylepšení. Například Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) může být použita k zabezpečenému zpřístupnění síťových schopností USS/UTM pro autorizaci služby a validaci letové trasy. Samotná komunikace může využívat buď přímý C2 spoj mezi řídicí stanicí a UAV, nebo nepřímý spoj prostřednictvím USS, v závislosti na operačním scénáři a regulatorních požadavcích. Systém podporuje jak unicastní, tak multicastní přenos pro efektivní šíření povelů při operacích s flotilami.

Služba zajišťuje, že C2 spoj splňuje přísné požadavky na dostupnost, integritu a nízkou latenci, které jsou klíčové pro bezpečný provoz UAV, zejména ve scénářích BVLOS. Toho je dosaženo prostřednictvím síťového řezání, vynucování QoS a nepřetržitého řízení konektivity včetně předávání spojení mezi buňkami při pohybu UAV. Architektura také zahrnuje bezpečnostní mechanismy pro zabránění neoprávněnému přístupu a ochranu C2 komunikace před odposlechem nebo manipulací v souladu s leteckými bezpečnostními standardy.

## K čemu slouží

Služba UAV-C byla vytvořena, aby řešila rostoucí potřebu spolehlivého velení a řízení dronů za hranicí přímé viditelnosti (BVLOS) s využitím všudypřítomných mobilních sítí. Před její standardizací byly operace dronů většinou omezeny na krátkodosahové přímé rádiové spoje (např. Wi-Fi nebo proprietární RF), což omezovalo operační dosah a komplikovalo integraci do řízeného vzdušného prostoru. Absence standardizovaného řešení C2 založeného na mobilních sítích bránila škálovatelným komerčním aplikacím dronů, jako je doručování, inspekce infrastruktury nebo letecké snímkování.

3GPP zahájila práci na podpoře UAV v Release 15, zpočátku se zaměřila na identifikaci a konektivitu. Release 17 konkrétně zavedlo službu UAV-C, aby poskytlo komplexní rámec pro autorizovanou C2 komunikaci, což umožňuje dronům bezpečně operovat na rozsáhlých územích. Tato standardizace řeší klíčové problémy: poskytuje zabezpečenou alternativu využívající licencované spektrum namísto nelicencovaných pásem, snižuje potřebu vlastní pozemní infrastruktury a usnadňuje regulatorní shodu nabídkou sledovatelných, autentizovaných spojů. Umožňuje plynulou mobilitu napříč pokrytím mobilní sítě, což je nezbytné pro dálkové mise dronů.

Motivace vychází z úsilí leteckého průmyslu směrem k UAS Traffic Management (UTM) a integraci dronů do národních systémů vzdušného prostoru. Využitím stávajících sítí 4G/5G snižuje UAV-C náklady na nasazení a urychluje uvedení na trh pro poskytovatele služeb s drony. Řeší omezení předchozích ad-hoc řešení, kterým chyběla interoperabilita, škálovatelnost a robustní funkce QoS a zabezpečení potřebné pro kritické C2 spoje ve sdíleném vzdušném prostoru.

## Klíčové vlastnosti

- Standardizovaná servisní architektura pro velení a řízení UAV přes sítě 3GPP
- Podpora přímých i nepřímých C2 komunikačních cest prostřednictvím UAV Service Supplier (USS)
- Integrace s UAS Traffic Management (UTM) pro autorizaci letů a správu vzdušného prostoru
- Rozšířené zabezpečení s autentizací, autorizací a ochranou integrity pro C2 spoje
- Vynucování QoS a síťové řezání pro zaručení nízkolatenčního a vysoce spolehlivého spojení
- Podpora mobility UAV s plynulým předáváním spojení a nepřetržitým řízením relace

## Související pojmy

- [UAV – Uncrewed Aerial Vehicle](/mobilnisite/slovnik/uav/)
- [UAS – NF Uncrewed Aerial System Network Function](/mobilnisite/slovnik/uas/)
- [UTM – Uncrewed Aerial System Traffic Management](/mobilnisite/slovnik/utm/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)

## Definující specifikace

- **TR 22.843** (Rel-19) — Study on Uncrewed Aerial Vehicle (UAV) Phase 3
- **TS 23.255** (Rel-19) — UAS Application Layer Support
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.755** (Rel-17) — Study on app layer support for UAS
- **TS 24.257** (Rel-19) — UAS Application Enabler (UAE) Layer
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 29.257** (Rel-19) — Application layer support for Uncrewed Aerial System (UAS)

---

📖 **Anglický originál a plná specifikace:** [UAV-C na 3GPP Explorer](https://3gpp-explorer.com/glossary/uav-c/)
