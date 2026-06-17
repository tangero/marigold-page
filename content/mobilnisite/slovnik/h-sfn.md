---
slug: "h-sfn"
url: "/mobilnisite/slovnik/h-sfn/"
type: "slovnik"
title: "H-SFN – Hyper System Frame Number"
date: 2025-01-01
abbr: "H-SFN"
fullName: "Hyper System Frame Number"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/h-sfn/"
summary: "Rozšířený čítač rámců používaný v LTE a NR, který poskytuje delší časovou referenci pro řídké nebo rozšířené cykly DRX, plánování vysílání informací a určování polohy. Umožňuje efektivní plánování pag"
---

H-SFN je rozšířený čítač rámců používaný v LTE a NR, který poskytuje delší časovou referenci pro řídké procedury, jako jsou rozšířené cykly DRX, plánování vysílání a určování polohy.

## Popis

Hyper System Frame Number (H-SFN) je klíčový časovací mechanismus definovaný ve specifikacích 3GPP Radio Access Network (RAN) pro LTE ([E-UTRA](/mobilnisite/slovnik/e-utra/)) i NR (New Radio). Funguje jako rozšíření konvenčního System Frame Number (SFN), který se cykluje od 0 do 1023, a poskytuje tak časovou referenci s delším trváním. H-SFN je 10bitová hodnota, která efektivně vytváří dvouúrovňovou hierarchickou časovou strukturu: standardní SFN se cykluje každých 10,24 sekundy, zatímco H-SFN se zvýší o jedničku pokaždé, když se SFN přeteče z 1023 na 0. Výsledkem je kombinovaný cyklus H-SFN+SFN o délce přibližně 2 hodiny, 55 minut a 50 sekund (1024 * 10,24 sekundy). Toto rozšířené časové rámce je zásadní pro plánování síťových procedur, které se vyskytují velmi řídce.

Z architektonického hlediska H-SFN udržuje základnová stanice sítě ([eNB](/mobilnisite/slovnik/enb/) v LTE, gNB v NR) a vysílá jej do všech uživatelských zařízení (UE) v buňce prostřednictvím systémových informací. Konkrétně je vysílán v MasterInformationBlock ([MIB](/mobilnisite/slovnik/mib/)) v NR a prostřednictvím vyhrazených SystemInformationBlocks (SIB) v LTE. UE používá tuto vysílanou hodnotu H-SFN k synchronizaci svého interního časování se sítí pro různé účely dlouhodobého plánování. Síť používá H-SFN k plánování vysílání dalších bloků systémových informací, pagingových příležitostí pro UE v rozšířeném režimu nečinnosti a ke koordinaci referenčních signálů pro určování polohy.

Fungování H-SFN je nedílnou součástí funkcí pro úsporu energie, jako je rozšířené nespojité příjímání (eDRX) a režim úspory energie (PSM). Pro eDRX, které může mít cykly trvající minuty nebo dokonce hodiny, H-SFN poskytuje hrubou časovou referenci potřebnou k určení konkrétního hyperrámce, ve kterém dojde k pagingovému časovému oknu (PTW) UE. Bez H-SFN by plánování tak dlouhých cyklů nebylo možné s omezeným rozsahem standardního SFN. Podobně pro plánování vysílacích kanálů jsou určité SystemInformationBlocks (např. SIB20 v LTE pro varovné zprávy) vysílány pouze v konkrétních periodách H-SFN, což snižuje síťovou režii a spotřebu energie UE zbytečným monitorováním.

V kontextu New Radio si H-SFN zachovává svou základní roli a je vysílán v MIB jako část pole systemFrameNumber, které nese kombinované nejvýznamnější bity ([MSB](/mobilnisite/slovnik/msb/)) H-SFN. Jeho použití bylo rozšířeno na podporu nových funkcí NR, jako je určování polohy, kde je vyžadováno přesné časování v dlouhých obdobích, a pro plánování dalších systémových informací s velmi dlouhými modifikačními periodami. H-SFN tedy slouží jako základní, škálovatelný časovací rámec, který podporuje pokročilé funkce RAN vyžadující rozšířenou časovou koordinaci mezi sítí a zařízením.

## K čemu slouží

H-SFN byl zaveden především pro podporu požadavků na úsporu energie pro komunikaci typu Machine-Type Communication ([MTC](/mobilnisite/slovnik/mtc/)) a zařízení Internetu věcí (IoT) v LTE, což byl hlavní zájem od 3GPP Release 13. Před jeho zavedením bylo síťové časování omezeno na 10,24sekundový cyklus SFN. Toto omezení představovalo významný problém pro plánování řídkých událostí, jako je paging zařízení používajících velmi dlouhé cykly eDRX nebo vysílání systémových informací, které se mění jen zřídka. Zařízení by se musela probouzet a monitorovat kanál příliš často, pokud by byla plánována pouze v rámci okna SFN, což by negovalo výhody dlouhé výdrže baterie hlubokých spánkových režimů.

Zavedení H-SFN to vyřešilo poskytnutím mnohem větší časové mřížky. To umožnilo síti jednoznačně plánovat události na dny nebo týdny dopředu pomocí H-SFN jako hrubého kalendáře a SFN pro jemné časování v rámci tohoto hyperrámce. Vyřešilo to omezení předchozího přístupu, kde bylo dlouhodobé plánování složité a vyžadovalo dodatečnou signalizační režii. Rozšířené časové rámce je také klíčové pro aplikace jako Earthquake and Tsunami Warning System (ETWS) a Commercial Mobile Alert System ([CMAS](/mobilnisite/slovnik/cmas/)), kde mohou být varovné zprávy platné po dlouhá období a potřebují být vysílány podle předvídatelného dlouhodobého plánu bez spotřeby nepřetržitých rádiových zdrojů.

Jak se sítě vyvíjely směrem k 5G NR, potřeba takových rozšířených časových referencí přetrvávala a rozšiřovala se. NR převzalo a formalizovalo koncept H-SFN, aby zajistilo zpětnou kompatibilitu v časovém návrhu pro nové scénáře IoT a massive MTC a podpořilo pokročilé služby jako ultra spolehlivá komunikace s nízkou latencí (URLLC) a vylepšené určování polohy, které také mohou těžit z dlouhodobých referenčních vzorů. H-SFN je tedy klíčovým prvkem umožňujícím energeticky efektivní připojení rozsáhlého množství zařízení a spolehlivé dlouhodobé plánování v moderních mobilních sítích.

## Klíčové vlastnosti

- 10bitové rozšíření SFN, vytvářející kombinovaný cyklus přibližně 2,9 hodiny
- Vysíláno v systémových informacích (MIB v NR, specifické SIB v LTE) pro synchronizaci UE
- Umožňuje plánování velmi dlouhých cyklů eDRX pro úsporu energie IoT zařízení
- Podporuje efektivní vysílání systémových informačních bloků, které se zřídka aktualizují
- Poskytuje dlouhodobou časovou referenci pro procedury určování polohy v NR
- Nezbytné pro plánování vysílání varovných zpráv (ETWS/CMAS) v rozšířených obdobích

## Související pojmy

- [MIB – Management Information Base](/mobilnisite/slovnik/mib/)

## Definující specifikace

- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.304** (Rel-19) — UE Idle Mode Procedures in E-UTRA
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.304** (Rel-19) — UE RRC_IDLE and RRC_INACTIVE Procedures
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.523** (Rel-19) — 5G NR UE Conformance Testing: Idle/Inactive

---

📖 **Anglický originál a plná specifikace:** [H-SFN na 3GPP Explorer](https://3gpp-explorer.com/glossary/h-sfn/)
