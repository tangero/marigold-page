---
slug: "lipf"
url: "/mobilnisite/slovnik/lipf/"
type: "slovnik"
title: "LIPF – Lawful Interception Provisioning Function"
date: 2025-01-01
abbr: "LIPF"
fullName: "Lawful Interception Provisioning Function"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/lipf/"
summary: "LIPF je síťová funkce 5G jádra odpovědná za zřizování konfiguračních dat pro zákonné odposlechy (LI) v jiných síťových funkcích (NF). Centralizuje správu parametrů souvisejících s LI, jako jsou identi"
---

LIPF je síťová funkce 5G jádra, která zřizuje konfigurační data pro zákonné odposlechy v jiných síťových funkcích a centralizuje správu parametrů, jako jsou identity cílů, pro jednotné vynucování.

## Popis

Lawful Interception Provisioning Function (LIPF) je standardizovaná síťová funkce ([NF](/mobilnisite/slovnik/nf/)) v architektuře 5G jádra (5GC), zavedená jako součást vylepšeného rámce pro zákonné odposlechy v systémech 5G. Jejím hlavním úkolem je sloužit jako centralizovaný bod pro zřizování všech konfiguračních dat souvisejících se zákonným odposlechem, která vyžadují různé odposlouchávající síťové funkce (I-NF) a funkce pro zákonný odposlech ([LIF](/mobilnisite/slovnik/lif/)). LIPF ukládá a spravuje příkazy k odposlechu, které obsahují podrobnosti, jako je identita cíle (např. SUPI, [MSISDN](/mobilnisite/slovnik/msisdn/)), rozsah odposlechu (např. obsah komunikací, informace související s odposlechem), oprávněné orgány a doba trvání příkazu. Tyto informace poskytuje ostatním NF na požádání nebo prostřednictvím mechanismů předplatného/oznámení.

Operačně, když je žádost o zákonný odposlech schválena, příslušný správní orgán (např. orgán činný v trestním řízení prostřednictvím funkce správy zákonného odposlechu) zřídí příkaz k odposlechu v LIPF. LIPF poté distribuuje potřebnou konfiguraci příslušným síťovým funkcím. Například může zřídit identitu cíle ve funkci správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)), aby se spustil odposlech při registraci cílového UE nebo vytvoření relace. Může také zřizovat data pro funkci správy relací ([SMF](/mobilnisite/slovnik/smf/)), funkci uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) nebo jiné NF zapojené do monitorování obsahu nebo shromažďování informací souvisejících s odposlechem. LIPF pro komunikaci s konzumními NF používá standardizovaná servisně orientovaná rozhraní, pravděpodobně založená na [HTTP](/mobilnisite/slovnik/http/)/2, což je v souladu se zásadami servisně orientované architektury 5GC.

LIPF hraje klíčovou roli v oddělení logiky zřizování od logiky provádění odposlechu. Tato centralizace zjednodušuje správu, zlepšuje možnost auditu a zajišťuje konzistenci. Zabraňuje nutnosti samostatné konfigurace každé jednotlivé NF pro úkoly odposlechu, což je zásadní v dynamickém, cloud-nativním prostředí 5G, kde lze NF pružně instanciovat a škálovat. LIPF komunikuje s funkcí pro zákonný odposlech (LIF), která zajišťuje zabezpečené doručování odposlechnutých dat do sběrné funkce. Správou toho, 'co' a 'koho' odposlouchávat, umožňuje LIPF I-NF soustředit se na 'jak' – na skutečnou technickou implementaci odposlechu určeného provozu nebo událostí pro zřízené cíle.

## K čemu slouží

LIPF byla vytvořena, aby řešila výzvy implementace zákonného odposlechu v servisně orientované architektuře (SBA) 5G jádra. Předchozí architektury 3GPP měly monolitičtější síťové prvky, kde se konfigurace [LI](/mobilnisite/slovnik/li/) často řešila prostřednictvím proprietárních nebo prvkově specifických správních rozhraní. S dekompozicí 5G na mnoho nezávisle škálovatelných síťových funkcí se ruční zřizování parametrů odposlechu napříč desítkami potenciálních instancí NF stalo provozně složitým, náchylným k chybám a pomalým.

Motivací pro standardizaci LIPF bylo poskytnout automatizovanou, centralizovanou a standardizovanou metodu pro zřizování příkazů k odposlechu. To řeší problém konzistence – zajištění, aby všechny relevantní NF měly stejné a aktuální informace o cílech odposlechu. Řeší také potřebu agility v cloud-nativních nasazeních, což umožňuje novým instancím NF automaticky získávat potřebnou konfiguraci LI. LIPF byla motivována regulačními požadavky, které ukládají povinnost efektivních a spolehlivých schopností zákonného odposlechu, což si vyžádalo moderní architektonický přístup odpovídající flexibilitě a distribuci sítí 5G při zachování přísných kontrol shody.

## Klíčové vlastnosti

- Centralizovaný úložiště a správce příkazů k zákonnému odposlechu
- Zřizuje konfiguraci odposlechu pro odposlouchávající síťové funkce (I-NF)
- Podporuje servisně orientovaná rozhraní pro integraci se síťovými funkcemi 5G jádra
- Spravuje identity cílů (SUPI, MSISDN), rozsah odposlechu a dobu trvání
- Umožňuje automatizovanou aktivaci a deaktivaci odposlechu v celé síti
- Zvyšuje možnost auditu a konzistenci konfigurace LI

## Definující specifikace

- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.128** (Rel-19) — 3GPP TS 33.128: Lawful Interception Protocols

---

📖 **Anglický originál a plná specifikace:** [LIPF na 3GPP Explorer](https://3gpp-explorer.com/glossary/lipf/)
