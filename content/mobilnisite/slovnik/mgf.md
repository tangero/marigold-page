---
slug: "mgf"
url: "/mobilnisite/slovnik/mgf/"
type: "slovnik"
title: "MGF – Media Gateway Function"
date: 2025-01-01
abbr: "MGF"
fullName: "Media Gateway Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mgf/"
summary: "Funkce jádra sítě, která převádí mediální toky mezi sítěmi s přepojováním okruhů (např. PSTN) a sítěmi s přepojováním paketů (např. IP). Je nezbytná pro interoperabilitu hlasových a videohovorů, proto"
---

MGF je funkce jádra sítě, která převádí mediální toky mezi sítěmi s přepojováním okruhů a sítěmi s přepojováním paketů, aby umožnila interoperabilitu služeb, jako jsou hlasové a videohovory.

## Popis

Media Gateway Function (MGF) je kritická komponenta v architektuře 3GPP, konkrétně v IP Multimedia Subsystem (IMS) a později v 5G Core (5GC). Jejím hlavním úkolem je sloužit jako překladový bod pro mediální provoz, který převádí mezi různými přenosovými a kódovacími formáty. Prakticky to znamená, že může přijmout tradiční hlasový tok [TDM](/mobilnisite/slovnik/tdm/) (Time-Division [Multiplexing](/mobilnisite/slovnik/multiplexing/)) z veřejné telefonní sítě ([PSTN](/mobilnisite/slovnik/pstn/)) nebo ze starší mobilní sítě 2G/3G a překódovat jej na paketový tok (jako [RTP](/mobilnisite/slovnik/rtp/) přes IP) pro přenos přes IP síť, a naopak. Tento proces zahrnuje nejen převod formátu, ale také potenciální úpravy kodeků, časovačů paketizace a potlačení ozvěn.

Z architektonického hlediska je MGF řízena samostatnou signalizační entitou, historicky Media Gateway Control Function ([MGCF](/mobilnisite/slovnik/mgcf/)) v IMS. Toto oddělení řídicí a mediální roviny (podle protokolu H.248/Megaco) umožňuje škálovatelný a flexibilní návrh sítě. MGCF zpracovává signalizaci relace (např. [SIP](/mobilnisite/slovnik/sip/), [ISUP](/mobilnisite/slovnik/isup/)), zatímco MGF provádí příkazy související s médii. V 5G Core je podobná funkčnost často integrována do User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) nebo poskytována vyhrazenými síťovými prvky pro propojení se staršími systémy. MGF má rozhraní k přenosovým sítím na obou stranách – k rozhraním okruhových trunků (např. E1/T1) i k rozhraním sítí s přepojováním paketů (např. Ethernet).

Její role přesahuje jednoduchý hlas. MGF dokáže zpracovávat videomediální toky a podporuje různé kodeky, jako jsou AMR, G.711 a EVS. Je klíčovým prvkem pro služby jako VoLTE (Voice over LTE) a VoNR (Voice over New Radio), když hovory potřebují být ukončeny v tradiční telefonní síti nebo z ní vycházet. Bez MGF by nebylo možné plynulé spojení mezi sítěmi nové generace s přepojováním paketů a rozsáhlou instalovanou základnou infrastruktury s přepojováním okruhů, což z ní činí základní kámen pro migraci sítí a kontinuitu služeb.

## K čemu slouží

MGF byla vytvořena, aby vyřešila základní problém interoperability mezi vznikajícími, efektivními sítěmi s přepojováním paketů (jako jsou ty založené na IP pro IMS a později 5G) a zavedenou globální telekomunikační infrastrukturou s přepojováním okruhů. Historicky byla veškerá telefonie založena na přepojování okruhů, což vyžadovalo vyhrazené fyzické nebo logické spojení po dobu trvání hovoru. Vzestup IP sliboval efektivnější využití šířky pásma a integrované služby, ale nemohl nativně komunikovat s PSTN. MGF poskytuje potřebný most.

Její vývoj byl motivován potřebou plynulé, postupné migrace ze starších sítí na plně IP sítě, jako je IMS. Operátoři nemohli svou celou síť nahradit přes noc. MGF jim umožnila zavádět jádrové sítě založené na IP a zároveň se připojovat k existujícím výnosným službám PSTN a odběratelům na starších mobilních generacích (2G/3G). Řešila omezení předchozích monolitických ústředen tím, že rozdělila bránu na samostatnou mediální rovinu (MGF) a řídicí rovinu (MGCF), podle paradigmatu architektury softswitch. Toto oddělení nabídlo větší škálovatelnost, interoperabilitu mezi dodavateli a možnost nezávislého upgradu řídicí logiky a schopností zpracování médií.

## Klíčové vlastnosti

- Překódování mezi mediálními toky s přepojováním okruhů (TDM) a s přepojováním paketů (IP/RTP)
- Podpora široké škály audio a video kodeků (např. G.711, AMR, EVS)
- Řízení pomocí protokolu H.248/Megaco z Media Gateway Controlleru (např. MGCF)
- Schopnosti potlačení ozvěn a generování/detekce tónů
- Rozhraní k TDM trunkům (E1/T1) i k IP síťovým rozhraním
- Nezbytná pro služby založené na IMS, jako je interoperabilita VoLTE s PSTN/CS sítěmi

## Související pojmy

- [MGCF – Media Gateway Control Function](/mobilnisite/slovnik/mgcf/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)
- [PSTN – Public Switched Telecommunications Network](/mobilnisite/slovnik/pstn/)

## Definující specifikace

- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.417** (Rel-7) — IMS Core Component for NGN Architecture
- **TS 23.517** (Rel-8) — IMS Core Component for NGN Architecture
- **TS 24.524** (Rel-19) — Hosted Enterprise Services Architecture

---

📖 **Anglický originál a plná specifikace:** [MGF na 3GPP Explorer](https://3gpp-explorer.com/glossary/mgf/)
