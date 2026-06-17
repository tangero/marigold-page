---
slug: "gttfe"
url: "/mobilnisite/slovnik/gttfe/"
type: "slovnik"
title: "GTTFE – Global Text Telephony Feature Environment"
date: 2025-01-01
abbr: "GTTFE"
fullName: "Global Text Telephony Feature Environment"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gttfe/"
summary: "Prostředí funkcí globální textové telefonie (Global Text Telephony Feature Environment, GTTFE) definuje konkrétní síťové komponenty, funkce a rozhraní potřebné k implementaci služby GTT. Poskytuje sta"
---

GTTFE je standardizovaný architektonický rámec, který definuje síťové komponenty, funkce a rozhraní potřebné k implementaci služby Global Text Telephony v sítích 3GPP.

## Popis

Prostředí funkcí globální textové telefonie (Global Text Telephony Feature Environment, GTTFE) je koncepční a architektonický rámec v rámci 3GPP, který specifikuje soubor síťových elementů, funkčních entit a referenčních bodů nezbytných k realizaci služby Global Text Telephony ([GTT](/mobilnisite/slovnik/gtt/)). Zavedené ve vydání 10 (Release 10) poskytuje strukturovaný model, který zajišťuje, že všechny implementace GTT dodržují společnou sadu schopností, a tím usnadňuje interoperabilitu mezi zařízeními od různých výrobců a v různých síťových nasazeních. GTTFE zahrnuje komponenty jak v uživatelském zařízení (UE), tak v jádru sítě, zejména v doméně IP Multimedia Subsystem (IMS), a podrobně popisuje, jak tyto elementy interagují při navazování, udržování a ukončování relací přenosu textu v reálném čase.

Z architektonického hlediska GTTFE zahrnuje klíčové funkce, jako je aplikační server GTT (GTT [AS](/mobilnisite/slovnik/as/)), který se nachází ve služební vrstvě IMS a vykonává servisní logiku pro textové relace, včetně řízení relace, propojování (interworking) a správy funkcí. Uživatelské zařízení (UE) musí obsahovat klientskou funkci GTT schopnou kódovat/dekódovat text pomocí protokolu T.140, vyjednávat mediální parametry prostřednictvím SIP/SDP a zpracovávat datový proud protokolu RTP (Real-time Transport Protocol) pro text. Jádrová síť, včetně brány paketové datové sítě (PGW) v EPS nebo funkce uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) v 5GC, je odpovědná za poskytování odpovídajících přenosových kanálů (bearer) s podporou QoS pro mediální proud textu. Dále jsou definovány funkce pro vzájemné propojení (Interworking Functions, IWFs), které překládají mezi paketově přepínaným textem GTT a staršími okruhově přepínanými systémy textové telefonie, čímž zajišťují zpětnou kompatibilitu.

Z provozního hlediska GTTFE definuje procedury pro vyvolání služby: když uživatel zahájí relaci GTT, UE signalizuje svou textovou schopnost prostřednictvím zpráv SIP do jádra IMS, které žádost směruje na GTT AS. AS řídí navázání relace a může přitom interagovat s funkcemi řízení politiky a účtování (Policy and Charging Control, PCC) za účelem zajištění potřebných zdrojů QoS z přístupové sítě. Během celé relace je textový proud přenášen přes RTP/UDP/IP, přičemž síť zajišťuje nízkou latenci a spolehlivost prostřednictvím vyhrazených přenosových kanálů EPS nebo 5G QoS toků. GTTFE také specifikuje rozhraní pro správu a účtování, což operátorům umožňuje sledovat využití služby a aplikovat odpovídající fakturační politiky. Tím, že GTTFE zahrnuje všechny tyto aspekty do jednotného prostředí, zajišťuje, že GTT není pouze samostatnou funkcí, ale integrovanou a spravovatelnou službou v rámci širšího ekosystému 3GPP.

## K čemu slouží

GTTFE bylo vytvořeno, aby vyřešilo potřebu standardizované a komplexní architektonické definice pro implementaci [GTT](/mobilnisite/slovnik/gtt/), protože dřívější vydání specifikací GTT byla poněkud roztříštěná v různých dokumentech 3GPP. Před vydáním 10 (Release 10) vyžadovalo nasazení GTT od síťových operátorů interpretaci a integraci různých funkčních požadavků z více specifikací, což vedlo k potenciálním problémům s interoperabilitou a nekonzistentním chováním služby. Motivací bylo sloučit všechny síťové komponenty související s GTT do jediného, uceleného funkčního prostředí, což zjednodušuje návrh sítě, testování a nasazení.

Historický kontext vychází z vývoje samotné služby GTT; jak služba nabývala na významu pro splnění regulatorních požadavků na dostupnost, bylo zřejmé, že je zapotřebí přísnější architektonický model, který by zajistil spolehlivá a škálovatelná nasazení. Vydání 10, které zavedlo GTTFE, bylo součástí širšího úsilí 3GPP o dozrání služeb založených na IMS a poskytnutí jasnějších plánů pro implementaci funkcí. Definováním GTTFE poskytlo 3GPP referenční architekturu, která explicitně nastiňuje role každého síťového elementu, jejich vzájemné interakce a potřebná rozhraní, čímž snižuje nejednoznačnost pro výrobce zařízení a poskytovatele služeb.

Tento rámec řeší problém závislosti na konkrétním dodavateli (vendor lock-in) a fragmentace služeb tím, že zajišťuje, aby všechny kompatibilní implementace GTT dodržovaly stejné strukturální principy. Umožňuje operátorům kombinovat síťové komponenty od různých dodavatelů při zachování funkčnosti služby end-to-end. Dále GTTFE usnadňuje zavádění nových vylepšení GTT v následujících vydáních, protože změny lze jasně lokalizovat na konkrétní komponenty v rámci prostředí. V konečném důsledku GTTFE podporuje širší cíl, aby se textová telefonie v reálném čase stala robustní službou na úrovni operátora (carrier-grade), která je stejně spolehlivá a všudypřítomná jako hlasová telefonie.

## Klíčové vlastnosti

- Definuje kompletní sadu síťových funkcí potřebných pro poskytování služby GTT
- Specifikuje referenční body a rozhraní mezi komponentami GTT pro zajištění interoperability
- Zahrnuje aplikační server GTT (AS) jako centrální entitu servisní logiky
- Zahrnuje klientské funkce v UE pro kódování textu, signalizaci SIP a zpracování RTP
- Integruje se s řízením politiky a účtování (PCC) pro dynamickou správu QoS
- Poskytuje architektonický model pro vzájemné propojení se staršími systémy textové telefonie

## Související pojmy

- [GTT – Global Text Telephony](/mobilnisite/slovnik/gtt/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 22.226** (Rel-19) — Global Text Telephony (GTT) Stage 1

---

📖 **Anglický originál a plná specifikace:** [GTTFE na 3GPP Explorer](https://3gpp-explorer.com/glossary/gttfe/)
