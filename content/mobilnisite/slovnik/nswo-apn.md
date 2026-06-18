---
slug: "nswo-apn"
url: "/mobilnisite/slovnik/nswo-apn/"
type: "slovnik"
title: "NSWO-APN – Non-Seamless WLAN Offload Access Point Name"
date: 2025-01-01
abbr: "NSWO-APN"
fullName: "Non-Seamless WLAN Offload Access Point Name"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nswo-apn/"
summary: "Vyhrazený APN používaný k směrování specifického uživatelského provozu přímo do sítě WLAN bez průchodu 3GPP core. Umožňuje odlehčení datového provozu na Wi-Fi pro zmírnění zahlcení a zvýšení nákladové"
---

NSWO-APN je vyhrazený název přístupového bodu (Access Point Name) používaný k směrování specifického uživatelského provozu přímo do sítě WLAN pro odlehčení, zcela obchází 3GPP core a neposkytuje kontinuitu relace.

## Popis

NSWO-APN (Non-Seamless [WLAN](/mobilnisite/slovnik/wlan/) Offload Access Point Name) je konfigurační prvek v architektuře 3GPP, který umožňuje odlehčení (offload) uživatelského datového provozu z mobilní sítě do bezdrátové lokální sítě (WLAN), jako je Wi-Fi, neseamless způsobem. Funguje jako logický identifikátor pro specifické připojení k paketové datové síti ([PDN](/mobilnisite/slovnik/pdn/)), které je určeno pro odlehčený provoz. Když se uživatelské zařízení (UE) připojí k síti a požádá o PDN připojení pomocí NSWO-APN, síťové funkce pro řízení politik, konkrétně Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) nebo Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)), tento [APN](/mobilnisite/slovnik/apn/) rozpoznají a uplatní politiky, které přesměrují přidružené toky provozu. Toto přesměrování obvykle probíhá na Packet Gateway ([PGW](/mobilnisite/slovnik/pgw/)) v 4G nebo na User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) v 5G, kde je provoz odpovídající politice [NSWO](/mobilnisite/slovnik/nswo/) směrován přímo na rozhraní lokální WLAN přístupové sítě namísto toho, aby byl přeposílán přes SGi nebo N6 rozhraní core networku do externí datové sítě.

Architektonicky je NSWO-APN klíčovou součástí frameworku ANDSF (Access Network Discovery and Selection Function) a později ATSSS (Access Traffic Steering, Switching and Splitting), ačkoli konkrétně představuje jednodušší, neintegrovanou metodu odlehčení. Proces je řízen operátorsky definovanými politikami provisionovanými v PCRF/PCF, které jsou komunikovány k bráně (PGW/UPF) přes referenční body Gx nebo N7. Tyto politiky specifikují filtry provozu (např. na základě cílové IP adresy, portu nebo aplikace), které mají být odlehčeny, když je UE připojeno přes WLAN přístupový bod, který je operátorem důvěryhodný. Samotné UE musí být tímto APN nakonfigurováno, často pomocí správy zařízení nebo počátečního provisioningu.

Role NSWO-APN je čistě pro směrování provozu a nezahrnuje žádný management mobility mezi 3GPP a WLAN. To znamená, že pokud UE opustí pokrytí WLAN, odlehčené IP relace jsou ukončeny a musí být znovu navázány přes mobilní rozhraní. Nedochází k zachování IP adresy ani k handover proceduře. Jeho implementace je klíčová pro síťové operátory, kteří chtějí využít hustá Wi-Fi nasazení ke zmírnění zahlcení licencovaného spektra, zejména v oblastech s vysokým provozem, jako jsou stadiony nebo městská centra, a zároveň nabídnout přímočarý, politikami řízený mechanismus pro správu toho, které služby (např. best-effort prohlížení internetu, aktualizace softwaru) jsou pro odlehčení vhodné.

## K čemu slouží

NSWO-APN byl zaveden, aby řešil rostoucí poptávku po mobilních datech a zahlcení v mobilních rádiových přístupových sítích. Operátoři potřebovali standardizovanou metodu pro odlehčení specifických typů datového provozu na doplňkové WLAN sítě, které často mají větší dostupnou šířku pásma a nižší cenu za bit. Primární motivací byla efektivita sítě: přesměrováním provozu, který nevyžaduje striktní mobilitu nebo záruky kvality služby (jako jsou aktualizace na pozadí nebo obecné prohlížení webu), na Wi-Fi mohlo být licencované mobilní spektrum zachováno pro služby v reálném čase, citlivé na zpoždění nebo s vysokou prioritou.

Historicky, před standardizovaným neseamless odlehčením, se operátoři spoléhali na proprietární řešení nebo jednoduchý výběr Wi-Fi na straně UE, kterému chyběla centralizovaná kontrola politik a který často vedl k suboptimálnímu uživatelskému zážitku (např. odlehčení kritického provozu na nekvalitní Wi-Fi). Zavedení NSWO-APN ve 3GPP Release 11 poskytlo standardizovaný, politikami řízený framework integrovaný do core networku. To umožnilo operátorům přesně definovat, které toky provozu mohou být odlehčeny na základě hluboké inspekce paketů, uživatelského předplatného a síťových podmínek, což zajišťovalo, že rozhodnutí o odlehčení jsou v souladu s obchodními a technickými cíli. Vyřešilo problém nespravovaného odlehčení tím, že dalo síti, nikoli pouze zařízení, kontrolu nad rozhodnutím o směrování.

## Klíčové vlastnosti

- Politikami řízené přesměrování provozu na základě operátorsky definovaných pravidel
- Používá vyhrazený APN k identifikaci PDN připojení určených pro odlehčení
- Odlehčuje provoz na PGW (4G) nebo UPF (5G) na lokální WLAN rozhraní
- Bez podpory kontinuity relace nebo mobility při změně přístupu
- Integruje se s PCRF/PCF pro dynamické vynucování politik přes rozhraní Gx/N7
- Typicky používán pro best-effort provoz ke zmírnění zahlcení mobilní sítě

## Související pojmy

- [APN – Access Point Name](/mobilnisite/slovnik/apn/)
- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [ANDSF – Access Network Discovery and Selection Function](/mobilnisite/slovnik/andsf/)
- [ATSSS – Access Traffic Steering, Switching, and Splitting](/mobilnisite/slovnik/atsss/)

## Definující specifikace

- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 29.212** (Rel-19) — Gx/Gxx/Sd/St Diameter Protocol
- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping
- **TS 29.215** (Rel-19) — S9 Reference Point Stage 3 Specification

---

📖 **Anglický originál a plná specifikace:** [NSWO-APN na 3GPP Explorer](https://3gpp-explorer.com/glossary/nswo-apn/)
