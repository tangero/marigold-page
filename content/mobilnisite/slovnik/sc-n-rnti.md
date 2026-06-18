---
slug: "sc-n-rnti"
url: "/mobilnisite/slovnik/sc-n-rnti/"
type: "slovnik"
title: "SC-N-RNTI – Single Cell Notification RNTI"
date: 2025-01-01
abbr: "SC-N-RNTI"
fullName: "Single Cell Notification RNTI"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sc-n-rnti/"
summary: "Dočasný identifikátor rádiové sítě používaný v LTE k upozornění UE na změny řídicího kanálu pro jednobuněčný multicast (SC-MCCH). Upozorňuje zařízení přihlášená k multicastovému příjmu, aby zkontrolov"
---

SC-N-RNTI je dočasný identifikátor rádiové sítě používaný v LTE k upozornění UE přihlášených k multicastovému příjmu na změny na řídicím kanálu pro jednobuněčný multicast (Single Cell Multicast Control Channel), což je vyzve ke kontrole aktualizovaných informací o službě.

## Popis

Single Cell Notification [RNTI](/mobilnisite/slovnik/rnti/) (SC-N-RNTI) je specifický typ dočasného identifikátoru rádiové sítě (RNTI) používaného v LTE rádiové přístupové síti pro operace jednobuněčného point-to-multipoint ([SC-PTM](/mobilnisite/slovnik/sc-ptm/)). RNTI je jedinečný identifikátor přiřazený eNodeB pro UE nebo skupinu UE, používaný ke scramblování a identifikaci zpráv řídicího kanálu na fyzickém downlinkovém řídicím kanálu ([PDCCH](/mobilnisite/slovnik/pdcch/)) nebo jeho vylepšené verzi ([EPDCCH](/mobilnisite/slovnik/epdcch/)). SC-N-RNTI má pevnou, předdefinovanou hexadecimální hodnotu (specifikovanou ve standardech 3GPP), kterou předem znají všechna UE podporující SC-PTM. Jeho jediným účelem je signalizovat oznámení nebo změnu na řídicím kanálu pro jednobuněčný multicast ([SC-MCCH](/mobilnisite/slovnik/sc-mcch/)), který nese konfigurační a plánovací informace pro dostupné SC-PTM služby.

Operačně eNodeB vysílá speciální PDCCH zprávu scramblovanou pomocí SC-N-RNTI. Tato zpráva neplánuje přenos žádných uživatelských dat; místo toho slouží jako indikátor podobný pagingu. Když UE zájemce o SC-PTM služby je ve stavu [RRC](/mobilnisite/slovnik/rrc/)_IDLE nebo RRC_CONNECTED, periodicky monitoruje PDCCH právě pro tento specifický RNTI. Detekce SC-N-RNTI na PDCCH je pro UE pokynem k okamžitému přečtení SC-MCCH. Samotný SC-MCCH je vysílán na [PDSCH](/mobilnisite/slovnik/pdsch/) v určitých modifikačních periodách a jeho obsah zahrnuje seznam dostupných transportních kanálů pro jednobuněčný multicast ([SC-MTCH](/mobilnisite/slovnik/sc-mtch/)), jejich odpovídající plánovací informace a přidružené skupinové RNTI (G-RNTI). Použitím SC-N-RNTI jako triggeru nemusí UE kontinuálně dekódovat SC-MCCH, což by spotřebovávalo značnou energii baterie. Dekódují jej pouze při signalizované změně, což je mnohem efektivnější.

Mechanismus SC-N-RNTI je klíčovou součástí návrhu pro úsporu energie v SC-PTM. Oznámení je broadcastováno všem UE v buňce podporujícím SC-PTM. eNodeB vysílá SC-N-RNTI na PDCCH během specifického časového okna v rámci modifikační periody SC-MCCH, typicky těsně před tím, než aktualizované informace SC-MCCH začnou platit. To zajišťuje, že UE mají dostatek času na získání nové konfigurace. SC-N-RNTI je součástí širšího prostoru RNTI v LTE, který zahrnuje další identifikátory jako C-RNTI (pro unicast), P-RNTI (pro paging), SI-RNTI (pro systémové informace) a G-RNTI používané k plánování skutečných přenosů dat SC-MTCH. Jeho pevná hodnota zajišťuje, že není vyžadován žádný dodatečný konfigurační signalizační přenos, aby jej UE rozpoznala, což zjednodušuje implementaci a zajišťuje interoperabilitu.

## K čemu slouží

SC-N-RNTI byl vytvořen k řešení problému efektivního oznamování a správy spotřeby energie pro UE přihlášené ke SC-PTM službám. V multicastových/broadcastových systémech je klíčovou výzvou informovat potenciálně velkou skupinu zařízení o změnách dostupnosti nebo konfigurace služeb bez nutnosti, aby každé zařízení neustále monitorovalo řídicí kanál, což by rychle vybilo baterii, zejména u IoT nebo zařízení pro veřejnou bezpečnost, která mohou potřebovat fungovat po dlouhou dobu.

Před mechanismy jako SC-N-RNTI mohla zařízení potřebovat periodicky se probouzet a dekódovat multicastový řídicí kanál (jako SC-MCCH) v jeho plné opakovací periodě, aby zkontrolovala aktualizace. To je neefektivní, pokud jsou aktualizace vzácné. SC-N-RNTI poskytuje asynchronní systém upozornění s nízkou režií. Umožňuje UE zůstat většinu času v stavu s nízkou spotřebou energie a aktivovat svůj plný přijímací obvod pouze pro monitorování PDCCH v krátkých periodách, kdy může být SC-N-RNTI vysílán. Tento návrhový vzor je podobný použití P-RNTI pro paging v idle módu, ale je specializovaný pro oznámení o multicastových službách.

Zavedený v 3GPP Release 13 spolu s širším rámcem SC-PTM byl SC-N-RNTI nezbytným prvkem pro praktické a energeticky efektivní multicastové služby na LTE, zejména pro komunikaci typu stroj-stroj a scénáře mission-critical push-to-talk. Řešil základní kompromis mezi dostupností služby a spotřebou energie zařízení, čímž učinil SC-PTM životaschopnou technologií pro vždy zapnuté nebo dlouhotrvající skupinové komunikační relace, kde zařízení musí být dosažitelná pro nová multicastová data bez nadměrných energetických nákladů.

## Klíčové vlastnosti

- Pevná, předdefinovaná hodnota RNTI známá všemi UE podporujícími SC-PTM.
- Používá se ke scramblování PDCCH příkazu, který signalizuje změnu na SC-MCCH.
- Umožňuje UE efektivně monitorovat aktualizace multicastových služeb bez kontinuálního dekódování SC-MCCH.
- Podporuje úsporu energie pro UE ve stavech RRC_IDLE i RRC_CONNECTED.
- Broadcastováno všem UE v buňce; není vyžadováno individuální přiřazení.
- Spouští v UE proces získání aktualizovaných informací SC-MCCH během jeho modifikační periody.

## Související pojmy

- [SC-MCCH – Single Cell Multicast Control Channel](/mobilnisite/slovnik/sc-mcch/)
- [SC-PTM – Single-Cell Point-to-Multipoint](/mobilnisite/slovnik/sc-ptm/)
- [RNTI – Radio Network Temporary Identifier](/mobilnisite/slovnik/rnti/)
- [P-RNTI – Paging Radio Network Temporary Identifier](/mobilnisite/slovnik/p-rnti/)
- [G-RNTI – GERAN Radio Network Temporary Identity](/mobilnisite/slovnik/g-rnti/)
- [PDCCH – Physical Downlink Control Channel](/mobilnisite/slovnik/pdcch/)

## Definující specifikace

- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [SC-N-RNTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/sc-n-rnti/)
