---
slug: "cngcf"
url: "/mobilnisite/slovnik/cngcf/"
type: "slovnik"
title: "CNGCF – Customer Network Gateway Configuration Function"
date: 2025-01-01
abbr: "CNGCF"
fullName: "Customer Network Gateway Configuration Function"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cngcf/"
summary: "CNGCF je řídicí funkce, která automatizuje konfiguraci brán zákaznických sítí (CNGs) v sítích 3GPP. Umožňuje poskytovatelům služeb vzdáleně zřizovat a spravovat CNGs, které propojují sítě v zákaznický"
---

CNGCF je řídicí funkce, která automatizuje konfiguraci brán zákaznických sítí (Customer Network Gateways) a umožňuje jejich vzdálené zřizování pro připojení zákaznických lokalit k mobilnímu jádru sítě kvůli službám jako je konvergence pevných a mobilních sítí.

## Popis

Customer Network Gateway Configuration Function (CNGCF) je síťová řídicí entita definovaná v rámci architektury 3GPP, konkrétně pro automatizovanou konfiguraci brán zákaznických sítí (CNGs). [CNG](/mobilnisite/slovnik/cng/) je síťové zařízení umístěné v zákaznické lokalitě (např. domácnost, kancelář, podnik), které zajišťuje konektivitu mezi místní zákaznickou sítí (např. Wi-Fi, Ethernet [LAN](/mobilnisite/slovnik/lan/)) a jádrem sítě mobilního operátora. CNGCF funguje jako centralizovaný konfigurační server, který komunikuje s CNGs pomocí standardizovaných protokolů za účelem doručení konfiguračních dat a zajištění jejich správného nastavení pro přístup k operátorským službám.

Z architektonického hlediska je CNGCF typicky implementována jako součást operátorského řídicího systému, často v rámci vrstev Network Management ([NM](/mobilnisite/slovnik/nm/)) nebo Element Management ([EM](/mobilnisite/slovnik/em/)). Rozhraní k CNG zprostředkovává přes referenční body správy s využitím protokolů jako TR-069 (CWMP) nebo NETCONF/YANG, jak je specifikováno v 3GPP. Základní činnost spočívá v tom, že CNGCF udržuje databázi konfiguračních profilů a politik. Když je nová CNG nasazena nebo potřebuje rekonfiguraci, CNGCF zařízení autentizuje, identifikuje požadovaný služební profil (na základě dat o účastníkovi, smluvních podmínek nebo umístění) a doručí příslušné konfigurační parametry. Tyto parametry mohou zahrnovat IP adresování, politiky QoS, bezpečnostní nastavení (jako koncové body tunelů [IPsec](/mobilnisite/slovnik/ipsec/)), směrovací informace a parametry specifické pro služby, jako je Voice over LTE (VoLTE) nebo připojení IoT.

Klíčové součásti funkčnosti CNGCF zahrnují její policy engine, který určuje, jakou konfiguraci použít; její zabezpečené komunikační rozhraní s CNGs; a její integraci s dalšími operátorskými systémy, jako je Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo Policy and Charging Rules Function (PCRF), pro získání kontextu o účastníkovi a politikách. CNGCF hraje zásadní roli v paradigmatu Zero-Touch Provisioning (ZTP), což umožňuje nasazení zákaznických zařízení v režimu plug-and-play bez manuálního technického zásahu. Tím se snižují provozní náklady, minimalizují se chyby v konfiguraci a umožňuje se rychlé škálování služeb. V širším síťovém kontextu CNGCF usnadňuje služby jako fixed wireless access, bezproblémový přechod mezi buněčnými a Wi-Fi sítěmi ([ATSSS](/mobilnisite/slovnik/atsss/)) a zabezpečené rozšíření podnikových sítí tím, že zajišťuje správnou integraci CNGs do rámce pro poskytování služeb operátora.

## K čemu slouží

CNGCF byla zavedena, aby řešila provozní výzvy spojené s manuální konfigurací tisíců či milionů brán zákaznických sítí (CNGs) nasazených na různých zákaznických lokalitách. Před její standardizací operátoři často spoléhali na manuální konfiguraci, předzásobení nebo proprietární protokoly pro automatickou konfiguraci, které nebyly škálovatelné, byly náchylné k chybám a bránily interoperabilitě mezi zařízeními [CNG](/mobilnisite/slovnik/cng/) od různých výrobců. Rozšíření konvergence pevných a mobilních sítí, služeb podnikových VPN a rezidenčního širokopásmového přístupu přes LTE/5G vytvořilo potřebu standardizovaného, automatizovaného způsobu vzdálené správy těchto hraničních zařízení.

Její vznik byl motivován posunem průmyslu k softwarově definovaným sítím a automatizovanému zřizování služeb. Definováním standardizované funkce v rámci 3GPP se zajišťuje, že jakákoli kompatibilní CNG může být nakonfigurována jakýmkoli kompatibilním řídicím systémem, což podporuje interoperabilitu mezi více výrobci. To řeší klíčové problémy, jako je zkrácení doby zavedení služby pro zákazníky, umožnění hromadného nasazení pro IoT a širokopásmový přístup a možnost dynamických aktualizací služeb (např. změna šířky pásma nebo bezpečnostních politik) bez fyzického přístupu k zařízení. Historicky je v souladu se širšími trendy automatizace správy sítí, které lze pozorovat ve standardech jako TR-069 Broadband Forum, ale je přizpůsobena pro ekosystém mobilních sítí 3GPP a integrována s mobilními politikami a daty účastníků.

## Klíčové vlastnosti

- Automatizované vzdálené zřizování a konfigurace brán zákaznických sítí (CNGs)
- Podpora Zero-Touch Provisioning (ZTP) pro umožnění nasazení zařízení v režimu plug-and-play
- Standardizované rozhraní (např. založené na TR-069 nebo NETCONF) pro interoperabilitu mezi více výrobci
- Integrace s policy systémy (např. PCRF) pro dynamické uplatňování QoS a služebních politik
- Zabezpečená řídicí komunikace včetně autentizace zařízení a šifrování dat
- Centralizovaná správa konfiguračních profilů a šablon pro různé typy služeb

## Související pojmy

- [CNG – Comfort Noise Generation](/mobilnisite/slovnik/cng/)

## Definující specifikace

- **TS 24.524** (Rel-19) — Hosted Enterprise Services Architecture
- **TS 24.525** (Rel-19) — Business Trunking Architecture & Requirements

---

📖 **Anglický originál a plná specifikace:** [CNGCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/cngcf/)
