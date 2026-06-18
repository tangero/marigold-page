---
slug: "bvc"
url: "/mobilnisite/slovnik/bvc/"
type: "slovnik"
title: "BVC – BSS GPRS Protocol Virtual Connection"
date: 2025-01-01
abbr: "BVC"
fullName: "BSS GPRS Protocol Virtual Connection"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/bvc/"
summary: "BVC je logické spojení v rámci rozhraní Gb, které přenáší signalizaci GPRS a uživatelská data mezi BSS a SGSN. Poskytuje virtuální point-to-point konektivitu pro zprávy protokolu BSSGP, což umožňuje e"
---

BVC je logické spojení v rámci rozhraní Gb, které přenáší signalizaci GPRS a uživatelská data mezi BSS a SGSN a poskytuje virtuální point-to-point konektivitu pro zprávy protokolu BSSGP.

## Popis

[BSS](/mobilnisite/slovnik/bss/) [GPRS](/mobilnisite/slovnik/gprs/) Protocol Virtual Connection (BVC) je základní koncept v architektuře GPRS, který vytváří logickou konektivitu mezi Base Station System (BSS) a Serving GPRS Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)) prostřednictvím rozhraní Gb. Každý BVC představuje virtuální point-to-point spojení, které přenáší zprávy protokolu [BSSGP](/mobilnisite/slovnik/bssgp/) (Base Station System GPRS Protocol), zahrnující jak signalizační informace, tak pakety uživatelských dat. BVC funguje na síťové vrstvě a poskytuje abstrakci, která odděluje správu logických spojení od podkladové fyzické transportní vrstvy, která typicky používá protokoly Frame Relay nebo IP.

Z architektonického hlediska každý BVC odpovídá konkrétní směrovací oblasti v rámci pokrytí BSS. Když se mobilní stanice připojí k síti GPRS, je přidružena ke konkrétnímu BVC na základě své aktuální polohy. BSS udržuje kontexty BVC, které zahrnují informace o směrovací oblasti, identifikátorech buněk a přidružených mobilních stanicích. SGSN obdobně udržuje kontexty BVC ke sledování logických spojení k různým prvkům BSS. Toto oboustranné řízení kontextu umožňuje koordinované směrování paketů a správu mobility při pohybu uživatelů mezi buňkami.

Z pohledu protokolu BVC funguje v rámci vrstvy BSSGP, která se v protokolovém zásobníku rozhraní Gb nachází nad vrstvou Network Service ([NS](/mobilnisite/slovnik/ns/)). Vrstva NS poskytuje fyzický přenos, zatímco BSSGP (a tím i BVC) zajišťuje správu logických spojení, řízení toku a parametry kvality služby. Každý BVC je identifikován jedinečným identifikátorem BVC ([BVCI](/mobilnisite/slovnik/bvci/)), který umožňuje jak BSS, tak SGSN rozlišovat mezi různými logickými spojeními. BVCI se používá ve všech zprávách BSSGP k zajištění správného směrování ke správnému logickému koncovému bodu.

Mechanismus BVC podporuje několik klíčových funkcí v sítích GPRS. Za prvé umožňuje efektivní směrování paketů tím, že poskytuje logické cesty pro downlinková data ze SGSN do BSS a uplinková data z BSS do SGSN. Za druhé podporuje správu mobility tím, že umožňuje SGSN sledovat, který BVC (a tedy kterou směrovací oblast) mobilní stanice aktuálně používá. Za třetí usnadňuje řízení toku prostřednictvím zpráv BSSGP pro řízení toku, které nezávisle spravují datový tok na každém BVC. Za čtvrté podporuje služby cell broadcast tím, že poskytuje logické kanály pro distribuci broadcast zpráv do více buněk.

Během provozu k vytvoření BVC dochází při inicializaci BSS nebo při konfiguraci nových směrovacích oblastí. BSS odesílá SGSN zprávy BVC-RESET k vytvoření nebo resetování kontextů BVC. Po vytvoření zůstává BVC aktivní, dokud není explicitně resetován nebo dokud nedojde k rekonfiguraci sítě. Správa BVC zahrnuje mechanismy pro zpracování chyb, kde zprávy BVC-FLUSH mohou v případě chyb vymazat data uložená v bufferu a zprávy BVC-BLOCK/UNBLOCK mohou dočasně pozastavit a obnovit provoz BVC pro účely údržby.

## K čemu slouží

Koncept BVC byl vyvinut k řešení základního problému spojení okruhově orientovaných Base Station Systems ([BSS](/mobilnisite/slovnik/bss/)) s paketově orientovanými jádry sítí [GPRS](/mobilnisite/slovnik/gprs/). Před GPRS komunikovaly prvky BSS s MSC (Mobile Switching Center) pomocí okruhově orientovaných protokolů optimalizovaných pro hlasová volání. Zavedení služeb paketových dat vyžadovalo nový přístup, který by dokázal zvládnout přerušovaný datový provoz, podporovat více současných spojení a poskytovat efektivní směrování bez nutnosti vytvářet fyzický okruh pro každou datovou relaci.

BVC vyřešil několik konkrétních problémů v raných nasazeních GPRS. Za prvé poskytl abstraktní logickou vrstvu, která umožnila, aby více virtuálních spojení sdílelo stejné fyzické transportní prostředky mezi BSS a SGSN. To bylo klíčové, protože vytváření vyhrazených fyzických okruhů pro každé paketové datové spojení by bylo neúměrně nákladné a neefektivní. Za druhé BVC umožnil oddělení provozu řídicí roviny (signalizace) a uživatelské roviny (data) v rámci stejného logického rámce, což umožnilo koordinovanou správu obou typů provozu. Za třetí podpořil požadavky na mobilitu uživatelů paketových dat tím, že poskytl logická spojení, která mohla být udržována při pohybu uživatelů mezi buňkami, aniž by vyžadovala fyzickou rekonfiguraci.

Historický kontext vývoje BVC byl přechod od hlasově orientovaných sítí 2G k sítím 2.5G s podporou dat. Stávající infrastruktura BSS musela být pro služby GPRS znovu využita, aby se minimalizovaly náklady na nasazení, ale tradiční protokoly rozhraní A nebyly vhodné pro paketová data. BVC jako součást sady protokolů BSSGP poskytl potřebnou adaptační vrstvu, která umožnila stávajícímu hardwaru BSS podporovat paketový přenos při zachování zpětné kompatibility s okruhově orientovanými službami. Tento přístup umožnil operátorům zavádět služby GPRS postupně bez nutnosti nahrazovat celou infrastrukturu rádiového přístupového sítě.

## Klíčové vlastnosti

- Abstrakce logického point-to-point spojení mezi BSS a SGSN
- Podpora více virtuálních spojení přes sdílené fyzické transportní prostředky
- Umožnění nezávislého řízení toku na virtuální spojení pomocí mechanismů BSSGP
- Poskytnutí logického seskupení na základě směrovací oblasti pro efektivní správu mobility
- Podpora přenosu jak signalizace (řídicí rovina), tak uživatelských dat (uživatelská rovina)
- Zahrnutí mechanismů pro obnovu po chybě prostřednictvím operací BVC-RESET a BVC-FLUSH

## Související pojmy

- [BSSGP – Base Station System GPRS Protocol](/mobilnisite/slovnik/bssgp/)
- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.228** (Rel-19) — IP Multimedia Service Requirements
- **TS 48.016** (Rel-19) — Gb Interface Network Service Specification

---

📖 **Anglický originál a plná specifikace:** [BVC na 3GPP Explorer](https://3gpp-explorer.com/glossary/bvc/)
