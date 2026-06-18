---
slug: "atsc"
url: "/mobilnisite/slovnik/atsc/"
type: "slovnik"
title: "ATSC – Advanced Television Systems Committee"
date: 2025-01-01
abbr: "ATSC"
fullName: "Advanced Television Systems Committee"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/atsc/"
summary: "ATSC je standard pro digitální televizní vysílání vyvinutý v Severní Americe, primárně pro pozemní vysílání. V kontextech 3GPP je na něj odkazováno v souvislosti se studiemi koexistence, analýzou ruše"
---

ATSC je severoamerický standard pro digitální televizní vysílání, na který se v 3GPP odkazuje v souvislosti se studiemi koexistence, rušení a sdílení spektra mezi mobilními sítěmi a vysílacími službami.

## Popis

Standard Advanced Television Systems Committee (ATSC) definuje soubor protokolů pro digitální televizní přenos, zahrnující kódování videa, kódování zvuku, transport a modulaci. Nejrozšířenější verze, ATSC 1.0, používá pro pozemní vysílání modulaci 8-VSB (Vestigial Sideband), pro video a kódování transportního proudu [MPEG-2](/mobilnisite/slovnik/mpeg-2/) a pro audio Dolby Digital. Systém je navržen pro robustní příjem ve stacionárních a přenosných scénářích, podporující služby televize standardního ([SD](/mobilnisite/slovnik/sd/)) a vysokého rozlišení ([HD](/mobilnisite/slovnik/hd/)) v šířce kanálu 6 MHz, typické pro severoamerická vysílací přidělení. Jeho architektura zahrnuje vysílač, který zpracovává audio, video a data do transportního proudu, aplikuje korekci chyb vpřed (Reed-Solomonovo a Trellisovo kódování) a moduluje signál pro přenos vzduchem.

Z pohledu 3GPP není ATSC mobilní technologií, ale kritickou stávající službou v konkrétních kmitočtových pásmech, zejména v pásmu 600 MHz (konkrétně rozsah 614-698 MHz). Specifikace 3GPP odkazují na ATSC v kontextu koexistence, rušení na sousedním kanále a potenciálu pro sdílení nebo přerozdělení spektra. Technické studie dokumentované v 3GPP TR a TS analyzují emisní masky, mimopásmové emise a charakteristiky přijímačů vysílačů ATSC za účelem definice potřebných ochranných pásem, limitů emisí základnových stanic a požadavků na UE při provozu mobilních sítí v sousedních kmitočtech. To zajišťuje, že nasazení LTE nebo 5G NR, zejména v pásmu 71 (600 MHz), nezpůsobí škodlivé rušení příjmu ATSC televize.

Interakce mezi systémy ATSC a 3GPP je řízena primárně prostřednictvím regulačních a technických omezení spíše než přímou interakcí protokolů. Plánování sítí pro mobilní operátory v pásmu 600 MHz musí brát v úvahu umístění a výkon vysílačů ATSC. Specifikace 3GPP definují požadavky na poměr úniku do sousedního kanálu ([ACLR](/mobilnisite/slovnik/aclr/)) a nežádoucí emise pro uživatelské zařízení (UE) a základnové stanice za účelem ochrany přijímačů ATSC. Dále studie o využití doplňkového downlinku ([SDL](/mobilnisite/slovnik/sdl/)) nebo dynamického sdílení spektra ve vysílacích pásmech berou charakteristiky pevného vysílání ATSC s vysokým výkonem jako primární omezení. Technická analýza zahrnuje komplexní modelování různých struktur signálu, úrovní výkonu a vzorů pokrytí mezi vysílací službou s vysokým výkonem a vysokými věžemi a nízkovýkonovou buněčnou mobilní sítí.

## K čemu slouží

ATSC byl vytvořen za účelem přechodu severoamerického televizního vysílání z analogového [NTSC](/mobilnisite/slovnik/ntsc/) na spektrálně efektivnější digitální formát vyšší kvality. Vyřešil problém omezeného vysílacího spektra tím, že umožnil více digitálních [SD](/mobilnisite/slovnik/sd/) kanálů nebo jeden [HD](/mobilnisite/slovnik/hd/) kanál ve stejném 6 MHz slotu, který byl dříve obsazen jedním analogovým kanálem. Také zavedl podporu pro prostorový zvuk, interaktivní služby a datové vysílání. Standard byl motivován globálním přechodem k digitální televizi, která ve srovnání se zastaralým analogovým standardem NTSC nabízela lepší kvalitu obrazu, odolnost proti rušení a nové možnosti služeb.

V rámci 3GPP je účel odkazování na ATSC a jeho studia zásadně odlišný. Nejde o implementaci ATSC, ale o zajištění pokojné a regulačně konformní koexistence rychle se rozšiřujících služeb mobilního širokopásmového připojení (LTE, 5G NR) se zavedenou kritickou vysílací infrastrukturou. Přerozdělení pásma 600 MHz (tzv. 'digitální dividenda' – spektrum uvolněné po vypnutí analogové TV) pro mobilní využití vytvořilo přímé sousedství mezi mobilními sítěmi a zbývajícími vysílači ATSC. Práce 3GPP byla nezbytná k technickému vymezení hranic této koexistence, specifikaci limitů emisí mobilních sítí za účelem prevence škodlivého rušení televizního příjmu, čímž umožnila úspěšnou aukci a nasazení cenného nízkopásmového spektra pro mobilní služby bez narušení veřejných vysílacích služeb.

## Klíčové vlastnosti

- Modulace 8-VSB pro robustní pozemní vysílání v 6 MHz kanálu
- Transportní proud MPEG-2 pro multiplexování videa, audia a dat
- Podpora televizních formátů standardního (SD) a vysokého rozlišení (HD)
- Kódování audia Dolby Digital (AC-3) pro možnosti prostorového zvuku
- Korekce chyb vpřed využívající Reed-Solomonovo a Trellisovo kódování
- Pevné vysílání s vysokým výkonem z vysokých věží pro širokoplošné pokrytí

## Související pojmy

- [LTE – Local Terminal Emulator](/mobilnisite/slovnik/lte/)

## Definující specifikace

- **TS 26.802** (Rel-19) — Multicast Enhancements for 5G Media Streaming
- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP
- **TR 26.942** (Rel-19) — Study on Media Energy Consumption Exposure & Evaluation
- **TR 26.949** (Rel-19) — TV Service Profiles for 3GPP Networks
- **TR 26.953** (Rel-19) — Study on Service Interactivity for Streaming & Download
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.761** (Rel-15) — Extended-Band 12 Study Report
- **TR 36.792** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [ATSC na 3GPP Explorer](https://3gpp-explorer.com/glossary/atsc/)
