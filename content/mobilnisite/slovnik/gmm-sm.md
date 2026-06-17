---
slug: "gmm-sm"
url: "/mobilnisite/slovnik/gmm-sm/"
type: "slovnik"
title: "GMM/SM – GPRS Mobility Management and Session Management"
date: 2025-01-01
abbr: "GMM/SM"
fullName: "GPRS Mobility Management and Session Management"
category: "Mobility"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/gmm-sm/"
summary: "GMM/SM zahrnuje protokoly a procedury pro správu mobility a paketových datových relací mobilního zařízení v sítích GPRS a UMTS. Zajišťuje funkce jako připojení/odpojení (attach/detach), aktualizace sm"
---

GMM/SM je soubor protokolů a procedur v sítích GPRS a UMTS, který spravuje mobilitu mobilního zařízení, paketové datové relace a IP konektivitu a zajišťuje funkce jako připojení (attach), aktualizace polohy a aktivace PDP kontextu.

## Popis

[GMM](/mobilnisite/slovnik/gmm/)/SM je základní soubor protokolů a procedur definovaných ve specifikacích 3GPP pro paketově přepínané jádrové sítě [GPRS](/mobilnisite/slovnik/gprs/) a UMTS. Působí mezi uživatelským zařízením (UE) a podpůrným uzlem pro GPRS (SGSN). GMM/SM je zodpovědný za dvě hlavní domény: správu mobility GPRS (GMM) a správu relací (SM). GMM spravuje mobilitu UE, sleduje jeho polohu a udržuje jeho registrační stav v síti. Klíčové procedury GMM zahrnují připojení a odpojení GPRS (Attach/Detach), které registrují a odregistrují UE v síti, a aktualizace směrovací oblasti (RAU), které informují síť o pohybu UE mezi směrovacími oblastmi. Tyto procedury zajišťují, že síť může efektivně vyvolávat (page) UE a směrovat datové toky směrem k uživateli (downlink) na jeho aktuální polohu.

Správa relací (SM) zajišťuje zřizování, modifikaci a ukončení paketových datových relací, známých jako PDP kontexty. PDP kontext definuje parametry datového připojení, včetně požadované kvality služeb (QoS), IP adresy přiřazené UE a přidruženého názvu přístupového bodu ([APN](/mobilnisite/slovnik/apn/)), který určuje konektivitu k externí paketové datové síti (např. internetu nebo podnikové intranetu). Procedury SM zahrnují signalizační výměny mezi UE a SGSN a mezi SGSN a bránovým podpůrným uzlem pro GPRS (GGSN) za účelem aktivace, modifikace nebo deaktivace těchto kontextů. Tím se vytvářejí přenosové kanály (bearers) v uživatelské rovině nezbytné pro přenos IP paketů.

Z architektonického hlediska jsou zprávy GMM/SM přenášeny přes vrstvu protokolu Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)). Tato vrstva je nezávislá na podkladové technologii rádiového přístupu (např. [GERAN](/mobilnisite/slovnik/geran/), UTRAN) a poskytuje konzistentní rozhraní pro správu mobility a relací v jádrové síti. SGSN funguje jako centrální uzel, koordinuje správu stavů GMM a předává signalizaci SM příslušnému GGSN. Robustnost a efektivita procedur GMM/SM jsou klíčové pro zajištění plynulé mobility a spolehlivých paketových datových služeb a tvoří páteř mobilní internetové konektivity v sítích 2,5G a 3G.

## K čemu slouží

[GMM](/mobilnisite/slovnik/gmm/)/SM byl vytvořen, aby poskytl standardizovaný rámec pro správu mobility a relací v paketově přepínaných mobilních sítích, konkrétně pro službu [GPRS](/mobilnisite/slovnik/gprs/) (General Packet Radio Service) zavedenou jako evoluce GSM. Před GPRS byly sítě GSM primárně okruhově přepínané, navržené pro hlasové hovory, což bylo pro přerušovaný (bursty) datový provoz neefektivní. Motivací bylo umožnit 'vždy zapojenou' (always-on) IP konektivitu, kde by zařízení mohlo udržovat logické připojení k síti bez vyčlenění nepřetržitého okruhu, a tím optimalizovat využití zdrojů pro datové aplikace.

Řešil problém správy mobilních zařízení v paketově přepínaném prostředí. Bez GMM by síť neznala polohu nečinného (idle) UE pro doručení příchozích dat, což by vedlo k neefektivnímu hromadnému vyvolávání (paging) nebo ztrátě paketů. Bez SM by neexistoval mechanismus pro dynamické zřizování a správu datových relací se specifickými profily QoS přizpůsobenými různým aplikacím (např. prohlížení webu vs. streamování videa). GMM/SM poskytl potřebné řídicí protokoly (control plane) pro sledování mobilních zařízení, jejich autentizaci a nastavování potřebných datových cest přes jádrovou síť, čímž umožnil efektivní mobilní datové služby.

Jeho vznik byl hnán rostoucí poptávkou po mobilních datech a přístupu k internetu na konci 90. let a počátkem 21. století. Položil základy pro paketové jádro UMTS (GPRS core network) a ovlivnil návrh pozdějších protokolů Evolved Packet System (EPS), jako je EPS Mobility Management ([EMM](/mobilnisite/slovnik/emm/)) a EPS Session Management (ESM) v 4G LTE, což demonstruje jeho zásadní roli ve vývoji mobilního širokopásmového připojení.

## Klíčové vlastnosti

- Procedury připojení/odpojení GPRS (Attach/Detach) pro registraci v síti
- Aktualizace směrovací oblasti (RAU) pro sledování polohy mobilního zařízení
- Aktivace, modifikace a deaktivace PDP kontextu
- Vyjednávání a správa QoS pro paketové datové relace
- Spolupráce s okruhově přepínanou mobilitou (prostřednictvím správy mobility GSM)
- Správa bezpečnostního kontextu pro autentizaci a šifrování

## Související pojmy

- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 43.318** (Rel-19) — Generic Access Network (GAN) Stage 2
- **TR 43.902** (Rel-19) — GAN Enhancements Feasibility Study
- **TS 44.318** (Rel-19) — Generic Access Network (GAN) Interface Procedures

---

📖 **Anglický originál a plná specifikace:** [GMM/SM na 3GPP Explorer](https://3gpp-explorer.com/glossary/gmm-sm/)
