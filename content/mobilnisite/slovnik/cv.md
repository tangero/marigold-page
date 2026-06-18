---
slug: "cv"
url: "/mobilnisite/slovnik/cv/"
type: "slovnik"
title: "CV – Conditional on Value"
date: 2025-01-01
abbr: "CV"
fullName: "Conditional on Value"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cv/"
summary: "CV (Conditional on Value) je mechanismus protokolu ve vrstvě Radio Resource Control (RRC) specifikace 3GPP, definovaný v TS 25.331. Umožňuje síti odesílat konfigurační zprávy k uživatelskému zařízení"
---

CV je mechanismus protokolu RRC v 3GPP, při kterém konfigurační zprávy pro UE obsahují nebo vynechávají informační prvky na základě hodnot jiných parametrů, aby se optimalizovala signalizace a snížila režie.

## Popis

Conditional on Value (CV) je sofistikovaná technika optimalizace signalizace zabudovaná do protokolu Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)), který řídí spojení mezi mobilním zařízením (UE) a [UTRAN](/mobilnisite/slovnik/utran/) (UMTS Terrestrial Radio Access Network). Funguje v jádře procesu kódování a dekódování zpráv RRC. Základní princip spočívá v tom, že přítomnost nebo obsah konkrétních informačních prvků ([IE](/mobilnisite/slovnik/ie/)) v rámci zprávy RRC je podmíněn hodnotou jiného, předcházejícího IE. Toto podmíněné zahrnutí je definováno formálními omezeními 'presence' a 'value' v rámci definic zpráv protokolu RRC v Abstract Syntax Notation One (ASN.1) v dokumentu 3GPP TS 25.331.

Z architektonického pohledu není CV samostatnou entitou, ale souborem pravidel uplatňovaných při konstrukci zprávy entitou RRC v řadiči rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)) a při interpretaci zprávy entitou RRC v UE. Když RNC potřebuje odeslat konfigurační zprávu (např. RADIO BEARER SETUP, RADIO BEARER RECONFIGURATION nebo PHYSICAL CHANNEL RECONFIGURATION), vyhodnotí konkrétní parametry, které mají být nastaveny. Na základě zvolené konfigurace pravidla CV určují, které IE musí být zahrnuty. Například, pokud je vybrán určitý typ transportního kanálu, jsou zahrnuty pouze IE relevantní pro tento typ kanálu, zatímco IE pro jiné, nevybrané typy kanálů jsou z přenášeného bitového toku zprávy zcela vynechány.

Fungování je zásadně spojeno s kódováním ASN.1 [PER](/mobilnisite/slovnik/per/) (Packed Encoding Rules). UE při přijetí zprávy postupuje podle stejných pravidel CV definovaných ve standardu, aby správně parsovalo zprávu proměnné délky. Přečte počáteční, řídící IE (podmínku) a na základě jeho dekódované hodnoty přesně ví, které následující IE má očekávat a dekódovat a které přeskočit. Tím se zabrání chybné interpretaci bitového toku. Tento mechanismus je klíčový pro zvládnutí obrovského kombinatorického prostoru možných konfigurací UE bez nutnosti mít pro každou z nich samostatnou, plně definovanou strukturu zprávy, která by byla neúměrně velká a neefektivní.

Jeho role v síti je především optimalizační a zajišťuje flexibilitu. Tím, že odstraňuje potřebu přenášet IE s výchozími nebo nepoužitelnými hodnotami, CV výrazně snižuje velikost signalizačních zpráv RRC. To šetří cenné rádiové zdroje, snižuje dobu přenosu, snižuje režii UE pro dekódování a minimalizuje signalizační latenci během kritických procedur, jako je předávání spojení a zřizování bearerů. Umožňuje, aby protokol RRC zůstal komplexní a vysoce konfigurovatelný pro podporu různých služeb (od hlasu po vysokorychlostní data) bez trvalé, maximální signalizační režie.

## K čemu slouží

Účelem mechanismu Conditional on Value (CV) je řešit kritický problém efektivity signalizace v mobilních sítích. Rané bezdrátové řídicí protokoly často používaly zprávy pevného formátu nebo obsahovaly všechny možné parametry bez ohledu na jejich relevanci pro konkrétní transakci. Když 3G UMTS přineslo mnohem složitější rádiové konfigurace s četnými volitelnými funkcemi a parametry, se tento přístup stal neudržitelným. Přenášení plných, nafouklých zpráv pro každou proceduru by spotřebovávalo nadměrnou šířku pásma na rozhraní vzduchem, zvyšovalo spotřebu baterie UE na zpracování a zavádělo zbytečná zpoždění při sestavování a rekonfiguraci spojení.

Historicky přechod od jednodušší signalizace GSM k bohatému, na služby zaměřenému protokolu [RRC](/mobilnisite/slovnik/rrc/) v UMTS vytvořil potřebu inteligentnější metody strukturování zpráv. Koncept CV byl zaveden, aby řešil omezení předchozích přístupů typu 'vše zahrnuto' nebo rigidně strukturovaných. Byl motivován potřebou zachovat zpětnou kompatibilitu a rozšiřitelnost; nové [IE](/mobilnisite/slovnik/ie/) mohly být přidány v pozdějších vydáních 3GPP a učiněny podmíněnými, aniž by se porušila logika parsování starších UE, která by nové podmíněné bloky jednoduše ignorovala na základě pravidel, kterým rozuměla.

V konečném důsledku CV existuje proto, aby umožnil funkčně bohaté, vysoce přizpůsobivé síťové řízení bez přidružené penalizace signalizační režie. Umožňuje síti odesílat přesné, kontextově specifické instrukce k UE. Tato optimalizace je zásadní pro udržení kvality služby, umožnění rychlých přechodů stavů a efektivní správu rádiových zdrojů pro rostoucí počet uživatelů a stále náročnější datové aplikace, čímž tvoří základní princip efektivity, který pokračoval i do návrhu RRC pro LTE a 5G NR.

## Klíčové vlastnosti

- Dynamické sestavování zpráv: Umožňuje síti konstruovat zprávy RRC, kde je zařazení informačních prvků dynamicky určováno hodnotou jiných parametrů.
- Redukce signalizační režie: Výrazně snižuje velikost zpráv řídicí roviny vynecháním IE, které obsahují výchozí, nulové nebo nepoužitelné hodnoty pro danou transakci.
- Kódování založené na pravidlech ASN.1: Implementováno prostřednictvím formálních omezení 'presence' a 'value' v rámci definic ASN.1 pro zprávy protokolu RRC, což zajišťuje jednoznačné kódování a dekódování.
- Návod pro parsování v UE: Poskytuje přijímajícímu UE implicitní mapu pro správné parsování zpráv proměnné délky na základě standardizovaných podmíněných pravidel.
- Flexibilita konfigurace: Podporuje širokou škálu možných konfigurací UE (např. různé transportní formáty, konfigurace měření, parametry předání spojení) v rámci jedné efektivní struktury zprávy.
- Základ zpětné kompatibility: Umožňuje vývoj protokolu, kde mohou být v pozdějších vydáních zavedeny nové, podmíněné IE, aniž by to ovlivnilo základní dekódovací logiku starších zařízení.

## Související pojmy

- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)

## Definující specifikace

- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [CV na 3GPP Explorer](https://3gpp-explorer.com/glossary/cv/)
