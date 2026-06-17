---
slug: "cc-rnti"
url: "/mobilnisite/slovnik/cc-rnti/"
type: "slovnik"
title: "CC-RNTI – Common Control Radio Network Temporary Identifier"
date: 2025-01-01
abbr: "CC-RNTI"
fullName: "Common Control Radio Network Temporary Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cc-rnti/"
summary: "CC-RNTI je identifikátor specifický pro uživatelské zařízení (UE), používaný v LTE a 5G NR pro plánování zpráv společného řídicího kanálu, jako je paging a změny systémových informací. Umožňuje efekti"
---

CC-RNTI je identifikátor specifický pro uživatelské zařízení (UE), používaný v LTE a 5G NR k efektivnímu plánování zpráv společného řídicího kanálu, jako je paging a systémové informace, pro cílené doručení konkrétnímu uživatelskému zařízení.

## Popis

Common Control Radio Network Temporary Identifier (CC-RNTI) je klíčový dočasný identifikátor rádiové sítě (RNTI) v rámci specifikací 3GPP LTE a NR, primárně definovaný pro plánování společných řídicích informací určených konkrétnímu uživatelskému zařízení (UE). Na rozdíl od vysílacích RNTI, jako je SI-RNTI (System Information) nebo P-RNTI (Paging), které adresují všechna UE v buňce, je CC-RNTI specifický pro konkrétní UE. Přiřazuje jej síť UE a používá se ke skramblování downlink řídicí informace ([DCI](/mobilnisite/slovnik/dci/)) na fyzickém downlink řídicím kanálu ([PDCCH](/mobilnisite/slovnik/pdcch/)) při plánování zpráv na fyzickém downlink sdíleném kanálu ([PDSCH](/mobilnisite/slovnik/pdsch/)), které obsahují společnou řídicí informaci určenou pro dané konkrétní UE.

Z architektonického hlediska CC-RNTI funguje v rámci vrstvy řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) a fyzické vrstvy (PHY) protokolového zásobníku rádiového rozhraní. Když síť potřebuje odeslat UE-specifickou pagingovou zprávu nebo aktualizovaný blok systémových informací (SIB), který se týká pouze určitých UE (např. prostřednictvím zpráv 'Paging' nebo 'SystemInformation'), použije k adresování DCI právě CC-RNTI. UE průběžně monitoruje PDCCH pro formáty DCI skramblované s přiřazenými RNTI. Po detekci DCI skramblovaného s jeho CC-RNTI ví, že má dekódovat přidružené přidělení prostředků PDSCH, aby přijalo společnou řídicí zprávu. Tento mechanismus odděluje plánovací povolení (na PDCCH) od vlastní datové části (na PDSCH).

Klíčovou rolí CC-RNTI je zvýšení efektivity signalizace a úspory energie UE. U pagingu umožňuje síť zavolat konkrétní UE bez nutnosti probouzet všechna UE v buňce k dekódování společné pagingové zprávy, což je výhodné pro IoT zařízení a obecně pro úsporu energie. U systémových informací může být použit k doručení konkrétních SIB nebo jejich aktualizací pouze těm UE, které je potřebují (např. UE v určitém stavu nebo podporující určité funkce), namísto jejich vysílání do celé buňky. Tento cílený přístup snižuje zbytečnou režii vysílání a zpracování na straně UE. Hodnota CC-RNTI je konfigurována signalizací [RRC](/mobilnisite/slovnik/rrc/) a je součástí kontextu UE v [eNB](/mobilnisite/slovnik/enb/)/gNB.

V provozu je CC-RNTI jedním z několika typů RNTI, z nichž každý má specifický účel. Jeho hodnotový prostor je odlišný od jiných RNTI, jako je [C-RNTI](/mobilnisite/slovnik/c-rnti/) (pro vyhrazený provoz) nebo RA-RNTI (pro náhodný přístup). Použití CC-RNTI je specifikováno v 3GPP TS 36.321 (specifikace MAC protokolu) pro LTE a jeho principy přecházejí i do NR. Představuje příklad konstrukční filozofie 3GPP, která využívá vyhrazené identifikátory pro specifické řídicí funkce k umožnění přesné, efektivní a škálovatelné síťové řídicí signalizace.

## K čemu slouží

CC-RNTI byl zaveden, aby vyřešil neefektivitu používání čistě vysílacích mechanismů pro řídicí informace, které jsou relevantní pouze pro podmnožinu UE. V raných vydáních LTE byly paging a aktualizace systémových informací vysílány všem UE v buňce pomocí společných RNTI (P-RNTI, SI-RNTI). To nutilo každé UE, bez ohledu na jeho individuální stav nebo potřeby, probudit se a dekódovat tyto zprávy, což vedlo k zbytečnému vybíjení baterie, zejména u zařízení s omezeným výkonem, jako jsou IoT senzory. Navíc vysílání všech změn systémových informací do celé buňky spotřebovávalo cenné rádiové prostředky a zvyšovalo latenci pro aktualizace, které se týkaly pouze specifických skupin UE.

Vytvoření CC-RNTI bylo motivováno potřebou granulárnější a efektivnější řídicí signalizace. Umožňuje cílené doručování, což síti dovoluje odesílat pagingové zprávy nebo specifické systémové informace pouze zamýšleným UE. Tím se snižuje celková signalizační zátěž na vysílacím kanálu, zlepšuje se spektrální účinnost a výrazně se zvyšuje úspora energie UE minimalizací dob probuzení a režie zpracování. Pro scénáře IoT a hromadné komunikace mezi stroji (mMTC) zavedené kolem Rel-13 je taková energetická účinnost prvořadá.

Historicky, před zavedením CC-RNTI, sítě postrádaly standardizovanou, efektivní metodu pro UE-specifické plánování společného řízení. Zatímco mohly existovat některé proprietární nebo méně efektivní metody, CC-RNTI poskytlo standardizované, škálovatelné řešení v rámci frameworku 3GPP. Vyřešilo omezení univerzálního vysílacího přístupu a připravilo cestu pro dynamičtější a efektivnější provoz sítě, zejména když se sítě vyvíjely k podpoře různorodých služeb s různými požadavky.

## Klíčové vlastnosti

- UE-specifické adresování pro zprávy společného řízení
- Umožňuje cílený paging ke snížení probouzení nesouvisejících UE
- Umožňuje efektivní doručování specifických aktualizací systémových informací
- Skrambluje downlink řídicí informaci (DCI) na PDCCH
- Konfigurováno prostřednictvím signalizace RRC jako součást kontextu UE
- Zvyšuje úsporu energie UE a efektivitu síťové signalizace

## Související pojmy

- [C-RNTI – Cell Radio Network Temporary Identifier](/mobilnisite/slovnik/c-rnti/)

## Definující specifikace

- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [CC-RNTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/cc-rnti/)
