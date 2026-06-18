---
slug: "sdap"
url: "/mobilnisite/slovnik/sdap/"
type: "slovnik"
title: "SDAP – Service Data Adaptation Protocol"
date: 2025-01-01
abbr: "SDAP"
fullName: "Service Data Adaptation Protocol"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sdap/"
summary: "SDAP je protokolová vrstva zavedená v 5G NR pro správu QoS toků mezi jádrem sítě a UE. Mapuje QoS toky na datové rádiové přenosy a označuje pakety identifikátory QoS toků, což umožňuje jemně odstupňov"
---

SDAP je protokolová vrstva 5G NR, která spravuje QoS toky mapováním na datové rádiové přenosy a označováním paketů identifikátory QoS toků pro diferenciaci služeb a podporu síťového řezání.

## Popis

Service Data Adaptation Protocol (SDAP) je podvrstva v uživatelské rovině protokolového zásobníku 5G New Radio (NR), která se nachází nad Packet Data Convergence Protocol ([PDCP](/mobilnisite/slovnik/pdcp/)) a pod aplikační vrstvou. Funguje transparentně mezi gNB (Next Generation NodeB) a uživatelským zařízením (UE). Její hlavní architektonická úloha spočívá v tom, že slouží jako adaptační vrstva pro rámec QoS definovaný pro 5G systém (5GS). Na rozdíl od LTE, kde bylo QoS svázáno s EPS přenosy, zavádí 5G flexibilnější model QoS založený na QoS tocích. Entita SDAP je konfigurována pro každou relaci Protocol Data Unit ([PDU](/mobilnisite/slovnik/pdu/)) a každý datový rádiový přenos ([DRB](/mobilnisite/slovnik/drb/)).

SDAP funguje tak, že zpracovává pakety ve směru downlink od User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) jádra sítě a pakety ve směru uplink od vyšších vrstev UE. Každý IP paket je asociován s konkrétním QoS Flow Identifier ([QFI](/mobilnisite/slovnik/qfi/)). Hlavní funkcí SDAP je mapovat tyto QoS toky na příslušné datové rádiové přenosy. Jeden DRB může přenášet pakety z více QoS toků, pokud sdílejí podobné charakteristiky QoS – tento proces se nazývá agregace QoS toků. Naopak, QoS tok s přísnými požadavky může být mapován na vyhrazený DRB. Toto mapování provádí entita SDAP v gNB ve směru downlink, zatímco entita SDAP v UE provádí zpětné mapování ve směru uplink na základě pravidel přijatých od sítě.

Klíčovým operačním mechanismem je označování paketů hlavičkami QFI. Ve směru downlink přidá vrstva SDAP v gNB k paketu malou SDAP hlavičku, která obsahuje QFI a případně [RQI](/mobilnisite/slovnik/rqi/) (Reflective QoS Indicator) a/nebo [RDI](/mobilnisite/slovnik/rdi/) (Reflective QoS Indication for Delay Critical [GBR](/mobilnisite/slovnik/gbr/)). Tato hlavička umožňuje UE identifikovat QoS tok, ke kterému paket patří, pro jeho správné zpracování ve směru uplink. Pro reflexivní QoS instruuje bit RQI UE, aby vytvořilo zrcadlové QoS pravidlo pro uplink na základě pozorovaného downlink provozu, čímž se snižuje signalizační režie. Vrstva SDAP je také zodpovědná za zpracování zřizování, modifikace a uvolňování entit SDAP a jejich přidružených mapování prostřednictvím signalizace RRC.

## K čemu slouží

SDAP byl vytvořen pro podporu revolučního modelu QoS 5G systému, který byl navržen tak, aby uspokojil nebývalou rozmanitost služeb – od rozšířeného mobilního širokopásmového připojení (eMBB) přes ultra-spolehlivé komunikace s nízkou latencí (URLLC) až po hromadný IoT (mIoT). Předchozí model 4G EPS přenosů byl relativně rigidní a vázal parametry QoS na přenosový tunel end-to-end. To ztěžovalo dynamické vytváření služeb a jemně odstupňovanou diferenciaci provozu. Model QoS v 5G odděluje QoS tok (koncept na úrovni služby) od datového rádiového přenosu (koncept na transportní úrovni), což umožňuje větší flexibilitu a efektivitu.

Tento protokol existuje, aby vyřešil problém efektivního mapování těchto abstraktních QoS toků na fyzické rádiové zdroje (DRB) při zachování integrity vynucování QoS. Umožňuje síti optimalizovat využití rádiových zdrojů agregací více podobných toků na jeden přenos nebo izolací kritických toků na vyhrazených přenosech, aniž by vyžadovala zapojení jádra sítě pro každou úpravu. Dále SDAP umožňuje síťové řezání tím, že poskytuje jasný demarkační bod, kde lze na mapování rádiových přenosů aplikovat politiky QoS specifické pro řez, přijaté od jádra sítě. Jeho zavedení bylo motivováno potřebou protokolového mechanismu, který by mohl realizovat pokročilý rámec QoS pro 5G a zajistit, aby různorodé požadavky na latenci, spolehlivost a šířku pásma mohly být technicky vynucovány na rozhraní vzdušného rozhraní.

## Klíčové vlastnosti

- Mapování QoS toků na DRB
- Označování QFI v hlavičkách paketů
- Podpora reflexivního QoS (RQI)
- Konfigurace pro každou relaci PDU
- Podpora asymetrického mapování pro uplink/downlink
- Zpracování reflexivního QoS pro Delay Critical GBR (RDI)

## Související pojmy

- [PDCP – Packet Data Convergence Protocol](/mobilnisite/slovnik/pdcp/)
- [QFI – QoS Flow Identifier](/mobilnisite/slovnik/qfi/)

## Definující specifikace

- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 37.324** (Rel-19) — Service Data Adaptation Protocol (SDAP)
- **TS 37.483** (Rel-19) — E1 Application Protocol (E1AP)
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.306** (Rel-19) — NR UE Radio Access Capability Parameters
- **TS 38.463** (Rel-19) — E1 Application Protocol (E1AP)

---

📖 **Anglický originál a plná specifikace:** [SDAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/sdap/)
