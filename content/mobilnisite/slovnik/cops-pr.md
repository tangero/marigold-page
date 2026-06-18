---
slug: "cops-pr"
url: "/mobilnisite/slovnik/cops-pr/"
type: "slovnik"
title: "COPS-PR – Common Open Policy Service - Policy Provisioning"
date: 2025-01-01
abbr: "COPS-PR"
fullName: "Common Open Policy Service - Policy Provisioning"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/cops-pr/"
summary: "COPS-PR je protokolové rozšíření COPS používané pro zřizování politik (policy provisioning) v sítích 3GPP. Umožňuje centralizovaným policy serverům zasílat konfigurační politiky síťovým prvkům, jako j"
---

COPS-PR je protokolové rozšíření COPS používané pro centralizované zřizování politik (policy provisioning) pro síťové prvky, jako jsou GGSN, které zajišťuje konzistentní uplatňování politik napříč sítěmi 3GPP.

## Popis

COPS-PR (Common Open Policy Service - Policy Provisioning) je protokol typu klient-server definovaný v rámci architektury Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)) standardu 3GPP. Funguje jako rozšíření základního protokolu [COPS](/mobilnisite/slovnik/cops/) ([RFC](/mobilnisite/slovnik/rfc/) 2748), které je speciálně navrženo pro scénáře zřizování (provisioning), nikoli pro outsourcování rozhodnutí. V tomto modelu plní funkci COPS-PR serveru Policy Decision Function ([PDF](/mobilnisite/slovnik/pdf/)), zatímco síťové prvky jako Gateway [GPRS](/mobilnisite/slovnik/gprs/) Support Node (GGSN) nebo Packet Data Network Gateway ([PDN-GW](/mobilnisite/slovnik/pdn-gw/)) fungují jako COPS-PR klienti.

Protokol pracuje nad [TCP/IP](/mobilnisite/slovnik/tcp-ip/) spojeními a vytváří mezi klienty a servery perzistentní relace. COPS-PR používá push model, ve kterém policy server proaktivně zasílá informace o politikách síťovým prvkům. Tyto informace zahrnují provisioningová data, jako jsou parametry QoS, pravidla účtování a politiky pro služební toky. Protokol využívá strukturu Policy Information Base ([PIB](/mobilnisite/slovnik/pib/)), která definuje konkrétní policy objekty a jejich atributy, které lze zřizovat. Tyto PIB jsou standardizovány ve specifikacích 3GPP, aby byla zajištěna interoperabilita mezi zařízeními různých výrobců.

Mezi klíčové komponenty COPS-PR patří Client Handle, který jednoznačně identifikuje každou klientskou relaci; Context Object, který specifikuje typ zpracovávaného požadavku; a Decision Object, který obsahuje samotné informace o zřizované politice. Protokol podporuje inkrementální aktualizace, což umožňuje serverům upravovat pouze konkrétní části dříve zřízených politik namísto opětovného zasílání kompletních sad politik. Tato efektivita je klíčová v rozsáhlých sítích, kde ke změnám politik dochází často.

V rámci architektury 3GPP slouží COPS-PR primárně rozhraní Gx mezi Policy and Charging Rules Function (PCRF) a Policy and Charging Enforcement Function (PCEF). Toto rozhraní je zásadní pro architekturu PCC, neboť umožňuje dynamické řízení politik pro relace účastníků. Prostřednictvím COPS-PR může PCRF zřizovat QoS politiky, pravidla účtování a rozhodnutí o propouštění (gating) pro PCEF, který tyto politiky následně uplatňuje na uživatelské datové toky. Spolehlivostní mechanismy protokolu zajišťují, že informace o politikách jsou konzistentně udržovány i při výpadcích sítě nebo restartech serveru.

## K čemu slouží

COPS-PR byl zaveden, aby vyřešil potřebu standardizovaného zřizování politik (policy provisioning) v sítích 3GPP. Před jeho přijetím bylo řízení politik často implementováno prostřednictvím proprietárních protokolů nebo manuální konfigurace, což vedlo k problémům s interoperabilitou a provozní neefektivitě. Růst paketových služeb a rostoucí složitost požadavků na QoS v sítích 3G vytvořily naléhavou potřebu automatizovaného, centralizovaného řízení politik.

Protokol řeší několik kritických problémů v řízení politik. Za prvé poskytuje standardizované rozhraní pro zřizování politik, což umožňuje interoperabilitu zařízení různých výrobců v sítích s řízením politik. Za druhé umožňuje aktualizace politik v reálném čase na základě měnících se síťových podmínek nebo profilů účastníků, čímž podporuje dynamické zřizování služeb. Za třetí snižuje provozní režii automatizací distribuce politik a zajištěním konzistence napříč síťovými prvky.

Historicky se COPS-PR stal preferovaným řešením oproti alternativním přístupům, protože využíval stávající rámec COPS a zároveň přidal specifická rozšíření pro scénáře zřizování. To umožnilo 3GPP stavět na IETF-standardizovaném protokolu namísto vytváření zcela nového řešení. Návrh protokolu specificky řeší požadavky telekomunikačních sítí, včetně podpory hierarchických struktur politik, spolehlivých mechanismů doručování a efektivních postupů aktualizace, které minimalizují spotřebu šířky pásma.

## Klíčové vlastnosti

- Standardizované rozhraní pro zřizování politik (policy provisioning) pro interoperabilitu zařízení různých výrobců
- Podpora inkrementálních aktualizací politik pro minimalizaci využití šířky pásma
- Spolehlivé mechanismy doručování s konfigurovatelnými časovači opakování
- Hierarchická struktura politik prostřednictvím definic Policy Information Base (PIB)
- Perzistentní TCP spojení s keep-alive mechanismy
- Podpora více policy kontextů v rámci jednotlivých klientských relací

## Související pojmy

- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [PCEF – Policy and Charging Enforcement Function](/mobilnisite/slovnik/pcef/)

## Definující specifikace

- **TS 32.101** (Rel-19) — Management principles and high-level requirements

---

📖 **Anglický originál a plná specifikace:** [COPS-PR na 3GPP Explorer](https://3gpp-explorer.com/glossary/cops-pr/)
