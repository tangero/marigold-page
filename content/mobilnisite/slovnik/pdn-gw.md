---
slug: "pdn-gw"
url: "/mobilnisite/slovnik/pdn-gw/"
type: "slovnik"
title: "PDN-GW – Packet Data Network Gateway"
date: 2025-01-01
abbr: "PDN-GW"
fullName: "Packet Data Network Gateway"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pdn-gw/"
summary: "Packet Data Network Gateway (PDN-GW nebo PGW) je uzel jádra sítě ve 4G Evolved Packet System (EPS), který slouží jako ukotvovací bod pro relaci uživatelského zařízení (UE) k externí paketové datové sí"
---

PDN-GW je uzel jádra sítě ve 4G EPS, který ukotvuje relaci uživatele k externí paketové datové síti, provádí přidělování IP adres a funguje jako primární brána k externím IP sítím.

## Popis

Packet Data Network Gateway (PDN-GW nebo [PGW](/mobilnisite/slovnik/pgw/)) je kritická síťová funkce v 3GPP Evolved Packet Core (EPC), specifikovaná napříč více releasy počínaje Rel-8 (LTE). Nachází se na hranici mezi důvěryhodnou EPC mobilního operátora a externími paketovými datovými sítěmi ([PDN](/mobilnisite/slovnik/pdn/)), jako je veřejný internet nebo privátní podnikové sítě. Pro každé uživatelské zařízení (UE) je PGW koncovým bodem [GTP](/mobilnisite/slovnik/gtp/) rozhraní S5/S8 od Serving Gateway ([SGW](/mobilnisite/slovnik/sgw/)) a výchozím bodem pro rozhraní SGi k externí PDN. Slouží jako mobilní kotva pro mobilitu mezi 3GPP přístupy (např. mezi LTE a 2G/3G) a je zodpovědná za správu IP konektivní relace UE.

Z architektonického hlediska PGW kombinuje několik klíčových funkcí. Je bodem vynucování politik, uplatňuje pravidla přijatá od Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) pro řízení přístupu, kontrolu šířky pásma a označování QoS. Provádí hlubokou inspekci paketů (DPI) k identifikaci datových toků služeb pro přesné účtování a aplikaci politik. PGW přiděluje IP adresu UE (IPv4, IPv6 nebo obojí), typicky pomocí [DHCP](/mobilnisite/slovnik/dhcp/) nebo z lokálního poolu, a funguje jako výchozí směrovač pro provoz UE. Také zajišťuje funkce účtování, generuje záznamy o účtování ([CDR](/mobilnisite/slovnik/cdr/)) pro offline účtování nebo komunikuje s Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)) pro řízení kreditu v reálném čase.

V oblasti zpracování paketů PGW směruje pakety v uplink směru od UE (přijaté přes GTP tunel od SGW) ven na externí PDN přes rozhraní SGi a pakety v downlink směru od PDN směruje do příslušného GTP tunelu směrem k SGW a nakonec k UE. Provádí klíčové bezpečnostní funkce, jako je filtrování paketů v uplink i downlink směru (funguje jako firewall), a může implementovat Network Address and Port Translation (NAPT), pokud jsou použity privátní IPv4 adresy. PGW také podporuje zákonný odposlech (LI) duplikováním a přesměrováním uživatelského provozu k orgánům činným v trestním řízení podle potřeby.

Se zavedením separace řídicí a uživatelské roviny (CUPS) v Release 14 byl monolitický PGW rozdělen na PGW-Control Plane (PGW-C) a PGW-User Plane (PGW-U). PGW-C zpracovává signalizaci (GTP-C, PFCP), správu relací a řízení politik, zatímco PGW-U pod kontrolou PGW-C přes protokol PFCP zajišťuje přenos paketů s vysokou propustností. To umožňuje nezávislé škálování prostředků řídicí a uživatelské roviny. V 5G jsou funkce PGW rozděleny mezi Session Management Function (SMF, řídicí rovina) a User Plane Function (UPF, uživatelská rovina), což pokračuje v paradigmatu CUPS.

## K čemu slouží

PDN-GW byl vytvořen jako součást Evolved Packet System (EPS) v 3GPP Release 8, aby poskytoval vysoce výkonnou, plně IP kotvící bránu pro sítě LTE. Konsolidoval a rozvinul funkce z 3G GGSN a přidal nové schopnosti vyžadované pro pokročilé služby LTE. Před EPS poskytoval GGSN základní IP konektivitu, ale postrádal integrované řízení politik a sofistikované účtování potřebné pro vrstvené datové služby a hlas založený na IMS (VoLTE).

PGW vyřešil potřebu jediné, stabilní mobilní kotvy v ploché, plně IP architektuře. V 3G mohl SGSN sloužit jako kotva pro některé scénáře mobility, což vedlo ke složitému směrování. Návrh EPS to zjednodušil tím, že z PGW učinil jedinou kotvu pro všechny 3GPP přístupy (LTE, 3G, 2G). Tento návrh minimalizoval ztrátu paketů a latenci během předávání spojení. Navíc jeho těsná integrace s PCRF přes rozhraní Gx umožnila dynamické, na službu orientované řízení politik a účtování, což bylo klíčové pro zpeněžení různých datových služeb (např. streamování videa vs. synchronizace na pozadí) a zajištění kvality pro aplikace v reálném čase.

Historicky PGW umožnil komerční nasazení LTE a přechod na mobilní broadband. Jeho schopnost přidělovat veřejné IP adresy, vynucovat politiky spravedlivého využívání a generovat podrobné záznamy o účtování tvořila provozní páteř služeb 4G. Pozdější zavedení CUPS (rozdělení PGW na PGW-C a PGW-U) řešilo omezení monolitických hardwarových zařízení, což operátorům umožnilo využívat cloudové, škálovatelné architektury a připravilo cestu pro servisně orientovanou architekturu jádra 5G. PGW zůstává klíčovým uzlem v současných 4G sítích a ve scénářích spolupráce s 5G.

## Klíčové vlastnosti

- Slouží jako mobilní kotva a IP relanční kotva pro UE v EPS
- Ukončuje GTP rozhraní S5/S8 a připojuje se k PDN přes SGi
- Přiděluje IP adresu(y) uživatelskému zařízení (UE) (IPv4/IPv6)
- Vynucuje politiky a pravidla účtování od PCRF (přes rozhraní Gx)
- Provádí směrování, přeposílání, filtrování a hlubokou inspekci paketů
- Generuje záznamy o účtování a podporuje zákonný odposlech

## Související pojmy

- [SGW – Signalling Gateway](/mobilnisite/slovnik/sgw/)
- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)
- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)

## Definující specifikace

- **TR 26.924** (Rel-19) — MTSI QoS Improvement Study
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.108** (Rel-19) — LI Handover Interface Specification

---

📖 **Anglický originál a plná specifikace:** [PDN-GW na 3GPP Explorer](https://3gpp-explorer.com/glossary/pdn-gw/)
