---
slug: "dms"
url: "/mobilnisite/slovnik/dms/"
type: "slovnik"
title: "DMS – Distribution Management System"
date: 2025-01-01
abbr: "DMS"
fullName: "Distribution Management System"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dms/"
summary: "Distribution Management System (DMS) je funkce správy sítě zodpovědná za distribuci, provizionování a správu softwaru, firmware, konfiguračních dat a dalších souborů do uživatelských zařízení (UE). Je"
---

DMS je funkce správy sítě zodpovědná za distribuci, provizionování (zavádění) a správu softwaru, firmware a konfiguračních souborů do uživatelských zařízení (UE) vzduchem (over-the-air).

## Popis

V rámci architektury 3GPP je Distribution Management System (DMS) síťová serverová funkce, která je součástí širšího rámce správy zařízení. Jejím hlavním úkolem je zpracovávat ukládání, doručování a správu objektů určených k distribuci do UE. Tyto objekty mohou zahrnovat softwarové aktualizace (např. firmware, záplaty operačního systému), konfigurační parametry, autentizační certifikáty, příkazy pro správu zařízení a soubory související s aplikacemi. DMS funguje jako úložiště a distribuční bod, který komunikuje s dalšími řídicími entitami, jako je Device Management ([DM](/mobilnisite/slovnik/dm/)) Server nebo aplikační server.

DMS spolupracuje s protokoly pro správu zařízení, jako je protokol Open Mobile Alliance Device Management ([OMA](/mobilnisite/slovnik/oma/) DM) nebo pozdější rámce. Proces obvykle začíná, když DM Server na základě zásad správy nebo spouštěče určí, že UE vyžaduje konkrétní objekt. DM Server následně komunikuje s DMS, aby objekt získal, nebo získá odkaz (např. [URI](/mobilnisite/slovnik/uri/)) na něj. Tento odkaz je zahrnut v řídicím příkazu odeslaném do UE prostřednictvím datového přenosového kanálu. UE po přijetí příkazu naváže samostatnou relaci pro stažení skutečného objektu z DMS pomocí standardních protokolů, jako je [HTTP](/mobilnisite/slovnik/http/) nebo [HTTPS](/mobilnisite/slovnik/https/). DMS je zodpovědný za zajištění bezpečného a spolehlivého doručení a může podporovat funkce jako rozdílové aktualizace, možnost pokračování v přerušeném stahování a priorizaci stahování.

Mezi klíčové architektonické komponenty patří samotný server DMS, jeho přidružená databáze pro ukládání distribučních objektů a rozhraní, která poskytuje. Primární rozhraní směřuje k DM Serveru (nebo jiné spouštěcí entitě) a je často založeno na [API](/mobilnisite/slovnik/api/) webových služeb. Rozhraní směrem k UE je typicky standardní rozhraní pro stahování dat. Role DMS je klíčová pro škálovatelnou a efektivní správu zařízení. Centralizuje ukládání velkých souborů, čímž odlehčuje tuto úlohu od více transakčně orientovaných DM Serverů, a umožňuje optimalizované mechanismy doručování (např. pomocí sítí pro doručování obsahu). Toto oddělení funkcí zvyšuje spolehlivost a výkon procesů provizionování a aktualizací vzduchem ([OTA](/mobilnisite/slovnik/ota/)), které jsou zásadní pro udržování bezpečnosti zařízení, zavádění nových funkcí a zajištění síťové kompatibility napříč rozsáhlým parkem různorodých zařízení.

## K čemu slouží

DMS byl zaveden, aby řešil rostoucí složitost a rozsah správy softwaru a konfiguračních dat pro masivní a různorodou populaci mobilních zařízení. Raná řešení správy zařízení často zahrnovala [DM](/mobilnisite/slovnik/dm/) Server jak pro zahajování řídicích akcí, tak pro hostování souborů ke stažení, což mohlo vést k problémům se škálovatelností, zejména při distribuci velkých aktualizací firmware milionům zařízení. Omezení tohoto integrovaného přístupu zahrnovala neefektivní využití serverových prostředků, nedostatek optimalizovaných mechanismů doručování a obtížnost správy různých verzí distribučních objektů.

Vytvoření specializovaného Distribution Management Systemu tyto problémy řeší oddělením řídicí logiky od funkce doručování obsahu. Toto architektonické rozdělení umožňuje síťovým operátorům nasadit pro DMS specializovanou infrastrukturu pro doručování obsahu s vysokou kapacitou, zatímco se DM Servery soustředí na zásady, plánování a správu relací zařízení. Motivací byla potřeba spolehlivých aktualizací OTA ve velkém měřítku, která se stala klíčovou s vývojem chytrých telefonů vyžadujících časté bezpečnostní záplaty a vylepšení funkcí. DMS poskytuje standardizované, centralizované úložiště, které zajišťuje konzistenci a kontrolu nad tím, jaké verze softwaru jsou k distribuci k dispozici.

V zásadě DMS existuje proto, aby umožnil efektivní, bezpečnou a řízenou hromadnou distribuci digitálních objektů do mobilních zařízení. Řeší provozní problém, jak spolehlivě nasazovat aktualizace a konfigurace do zařízení v terénu, aniž by byly přetíženy síťové nebo serverové prostředky, a tím zajišťuje, aby zařízení zůstala bezpečná, funkční a schopná podporovat nové síťové služby. To je základním kamenem moderní správy životního cyklu zařízení a je stále důležitější i pro správu zařízení IoT.

## Klíčové vlastnosti

- Centralizované úložiště pro softwarové, firmware a konfigurační soubory
- Oddělení řídicí logiky (DM Server) od doručování obsahu
- Podporuje standardní stahovací protokoly (HTTP/HTTPS) pro přístup UE
- Umožňuje škálovatelné doručování velkých objektů masivnímu počtu zařízení
- Může poskytovat deskriptory stahování a URI pro spuštění stahování v UE
- Usnadňuje správu verzí a správu distribučních objektů

## Související pojmy

- [OTA – Over The Air](/mobilnisite/slovnik/ota/)

## Definující specifikace

- **TR 22.804** (Rel-16) — 5G Automation in Vertical Domains Study
- **TS 24.141** (Rel-19) — Presence Service Protocol Details
- **TS 24.247** (Rel-19) — IMS Messaging Service Protocol Details
- **TS 24.841** (Rel-6) — Presence Service IP Multimedia Subsystem
- **TS 29.199** (Rel-9) — Multimedia Messaging Web Services
- **TS 32.827** (Rel-10) — UE Management over Itf-N for MDT/SON

---

📖 **Anglický originál a plná specifikace:** [DMS na 3GPP Explorer](https://3gpp-explorer.com/glossary/dms/)
