---
slug: "kik"
url: "/mobilnisite/slovnik/kik/"
type: "slovnik"
title: "KIK – Key Identifier for protecting KIc and KID"
date: 2002-01-01
abbr: "KIK"
fullName: "Key Identifier for protecting KIc and KID"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/kik/"
summary: "Identifikátor klíče používaný v raných specifikacích 3GPP k odkazování na šifrovací klíč (KIc) a integritní klíč (KID) v bezpečnostních procedurách. Slouží jako index nebo štítek pro aktivní sadu klíč"
---

KIK je identifikátor klíče používaný v raných specifikacích 3GPP k odkazování na šifrovací klíč (KIc) a integritní klíč (KID), který slouží jako index pro aktivní sadu klíčů v bezpečnostních procedurách.

## Popis

Identifikátor klíče pro ochranu KIc a KID (KIK) je bezpečnostní parametr definovaný ve specifikacích 3GPP Release 5, primárně v kontextu bezpečnostní architektury 3G. Slouží jako identifikátor nebo referenční ukazatel, který označuje, která konkrétní dvojice šifrovacích a integritních klíčů (KIc a KID) je právě používána nebo má být použita pro zabezpečení komunikace mezi uživatelským zařízením (UE) a sítí. KIc je šifrovací klíč používaný pro ochranu důvěrnosti dat a signalizace, zatímco KID je integritní klíč používaný k zajištění, že data a signalizace nebyly pozměněny. KIK sám neobsahuje materiál klíčů, ale odkazuje na sadu klíčů uloženou zabezpečeně jak v UE, tak v Authentication Centre (AuC) nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) sítě.

Architektonicky je KIK součástí bezpečnostního kontextu vytvořeného během procedur autentizace a dohody o klíčích ([AKA](/mobilnisite/slovnik/aka/)). Když se UE autentizuje u sítě, AuC/HSS vygeneruje jako součást AKA vektoru šifrovací klíč ([CK](/mobilnisite/slovnik/ck/)) a integritní klíč ([IK](/mobilnisite/slovnik/ik/)). Tyto klíče (CK/IK) mohou být dále transformovány nebo namapovány na přístupové klíče KIc a KID pro použití v konkrétních doménách, jako je Circuit Switched ([CS](/mobilnisite/slovnik/cs/)) nebo Packet Switched (PS) jádro. KIK je asociován s touto odvozenou sadou klíčů. Je přenášen mezi síťovými entitami (např. z HSS na Visitor Location Register (VLR) nebo Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN)) v rámci signalizačních zpráv, jako je protokol [MAP](/mobilnisite/slovnik/map/) (Mobile Application Part), aby naznačil, které klíče má obslužná síť použít.

Během provozu, když je iniciován příkaz security mode pro zahájení šifrování a integritní ochrany na rádiovém spojení, síť zahrne KIK do signalizace směrem k UE. UE, které si z autentizační procedury předtím uložilo jednu nebo více sad klíčů (každá s odpovídajícím KIK), použije přijatý KIK k identifikaci a výběru správných KIc a KID ze své lokální paměti. Obě strany pak použijí tyto identifikované klíče k inicializaci šifrovacích a integritních algoritmů (např. UEA nebo UIA v UMTS). Tento mechanismus umožňuje správu klíčů, včetně změny klíčů nebo použití více současných bezpečnostních kontextů, prostým odkazováním na různé hodnoty KIK.

Jeho role byla v raném 3G zabezpečení klíčová pro umožnění aktualizace a správy klíčů bez nutnosti častého přenosu skutečných klíčů vzduchem. Použitím identifikátoru mohl systém efektivně přepnout na nové klíče (např. po změně lokace nebo periodické autentizaci) a zajistit synchronizaci mezi UE a sítí. Koncept samostatného KIK pro KIc/KID byl však v pozdějších vydáních 3GPP (jako LTE a 5G) z velké části nahrazen integrovanějšími hierarchiemi klíčů, kde jsou klíče identifikovány implicitně pomocí parametrů odvození klíčů nebo specifických identifikátorů sad klíčů v rámci širšího bezpečnostního kontextu. KIK představuje raný, explicitní mechanismus indexování klíčů ve vývoji zabezpečení mobilních sítí.

## K čemu slouží

KIK byl vytvořen k řešení potřeby efektivní a bezpečné správy klíčů v sítích 3G UMTS. Při přechodu ze sítí 2G (GSM) na 3G bylo zabezpečení významně posíleno zavedením vzájemné autentizace a samostatné integritní ochrany vedle šifrování. To vedlo ke dvěma klíčům na relaci: KIc pro šifrování a KID pro integritu. Byl vyžadován mechanismus, který by umožnil síti jednoznačně sdělit UE, kterou dvojici klíčů má použít, zejména proto, že mohlo být uloženo více sad klíčů z předchozích autentizací nebo pro různé servisní domény.

Předchozí přístupy v GSM používaly jediný šifrovací klíč (Kc) s méně sofistikovanou správou. Zavedení identifikátoru klíče vyřešilo problém synchronizace a výběru klíčů. Bez identifikátoru by síť a UE mohly ztratit shodu ohledně toho, který klíč je aktuální po předání spojení nebo během souběžných služeb, což by vedlo k selhání komunikace nebo bezpečnostním zranitelnostem. KIK poskytl jednoduchý index pro udržení této shody, což umožnilo funkce jako změna klíče za běhu bez opětovné autentizace distribucí nové sady klíčů s novým KIK.

Jeho vývoj v Release 5 byl součástí širšího bezpečnostního rámce 3G definovaného v TS 33.102 a souvisejících specifikacích jako TS 23.048. Usnadnil oddělení generování klíčů v domovské síti (AuC/[HSS](/mobilnisite/slovnik/hss/)) od používání klíčů v obslužné síti (VLR/SGSN), protože obslužná síť mohla odkazovat na klíče pomocí KIK, aniž by sama musela zpracovávat logiku odvození klíčů. Jak se však bezpečnostní architektury vyvíjely směrem k LTE a 5G, hierarchie klíčů se stala složitější a založenou na odvozování, což snížilo potřebu takových explicitních samostatných identifikátorů. Účel KIK byl efektivně absorbován do komplexnějších identifikátorů klíčů a schémat odvozování, což z něj činí historický, ale důležitý krok ve vývoji správy klíčů v mobilním zabezpečení.

## Klíčové vlastnosti

- Identifikátor používaný k odkazování na konkrétní dvojici šifrovacích (KIc) a integritních (KID) klíčů
- Umožňuje synchronizaci výběru klíčů mezi UE a síťovými entitami
- Podporuje správu klíčů a použití více uložených bezpečnostních kontextů
- Přenášen v síťové signalizaci (např. MAP zprávy) k označení aktivní sady klíčů
- Umožňuje změny klíčů bez okamžité opětovné autentizace
- Součást bezpečnostní architektury 3G UMTS definované v raných vydáních

## Definující specifikace

- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management

---

📖 **Anglický originál a plná specifikace:** [KIK na 3GPP Explorer](https://3gpp-explorer.com/glossary/kik/)
