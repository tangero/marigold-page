---
slug: "ift"
url: "/mobilnisite/slovnik/ift/"
type: "slovnik"
title: "IFT – Internet Facsimile Transfer"
date: 2025-01-01
abbr: "IFT"
fullName: "Internet Facsimile Transfer"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ift/"
summary: "IFT je služba 3GPP umožňující přenos faxových dokumentů přes IP sítě, konkrétně přes IMS. Definuje protokoly a postupy pro adaptaci tradičního faxu skupiny 3 pro přenos v reálném čase přes moderní pak"
---

IFT je služba 3GPP, která umožňuje přenos faxových dokumentů přes IP sítě, jako je IMS, přizpůsobením tradičního faxu pro přenos v reálném čase přes paketové sítě.

## Popis

Internet Facsimile Transfer (IFT) je standardizovaná služba v rámci architektury IP Multimedia Subsystem (IMS) dle 3GPP, specifikovaná primárně v TS 26.114. Poskytuje schopnost odesílat a přijímat faxové dokumenty v čistě IP prostředí, čímž propojuje starší faksimilní technologii s moderními paketovými sítěmi. Služba podporuje dva základní režimy provozu: přenos v hlasovém pásmu (VBD) a paketový přenos podle T.38. V režimu VBD jsou signály faxového modemu považovány za audio, kódované pomocí kodeku jako G.711 a přenášené v rámci hlasové relace IMS. V režimu T.38 jsou signály faxového modemu demodulovány a paketizovány do specifického protokolu (T.38) pro robustnější přenos přes IP sítě, které mohou mít ztrátu paketů, zpoždění nebo jitter.

Architektonicky zahrnuje IFT několik klíčových síťových funkcí. Uživatelské zařízení (UE) musí podporovat funkčnost faxového modemu a příslušné klientské schopnosti pro IMS. Jádro IMS zajišťuje navázání relace pomocí SIP (Session Initiation Protocol) a SDP (Session Description Protocol) pro vyjednání režimu faxu a parametrů. Na zpracování médií se mohou podílet prostředky jako Media Resource Function Processor ([MRFP](/mobilnisite/slovnik/mrfp/)), zejména při transkódování nebo propojování protokolů, a to hlavně ve scénářích zahrnujících přechod mezi okruhově přepínanou a paketově přepínanou doménou (např. fax do/z linky PSTN). Služba definuje specifické formáty přenášených dat, postupy pro vyjednávání relace a záložní mechanismy pro zajištění interoperability.

Fungování IFT začíná iniciací relace. UE ve své SIP INVITE zprávě indikuje schopnost a záměr vést faxovou relaci. Síť službu autorizuje a směruje relaci. Během fáze přenosu médií faxové modemy provedou svůj standardní handshake a tréninkové procedury, ale audio nebo datové pakety jsou přenášeny přes přenosový kanál IMS. Pro režim T.38 UE nebo síťová brána převádí [HDLC](/mobilnisite/slovnik/hdlc/) rámce faxu do T.38 UDPTL nebo TCP paketů. IFT zahrnuje postupy pro řešení síťových událostí, jako jsou změny kodeku, aktualizace relace a chybové stavy specifické pro faxový přenos, čímž zajišťuje spolehlivé doručení faxového dokumentu od konce ke konci.

## K čemu slouží

IFT byla vytvořena, aby řešila sice klesající, ale stále přetrvávající potřebu faxových služeb ve světě přecházejícím na čistě IP telekomunikační sítě. Tradiční fax přes okruhově přepínané sítě (PSTN/[ISDN](/mobilnisite/slovnik/isdn/)) byl nekompatibilní s paketovou povahou mobilních jader 3G/4G/5G a IMS. Účelem IFT je poskytnout standardizovanou, operátorsky vhodnou metodu pro podporu faxu přes tyto nové sítě, což zajišťuje kontinuitu podnikání pro sektory jako zdravotnictví, právo nebo logistika, které se na přenos dokumentů faxem stále spoléhají kvůli právní uznávanosti nebo integraci se staršími systémy.

Motivace vycházela ze zavedení IMS jako platformy pro poskytování multimediálních komunikací. Bez standardu jako IFT by se operátoři potýkali s proprietárními řešeními, problémy s interoperabilitou a neschopností nabídnout spolehlivou faxovou službu svým mobilním i pevným zákazníkům v sítích nové generace. IFT řeší problém přenosu signálů faxového modemu v reálném čase přes IP síť náchylnou k poškození paketů. Standardizací přístupů VBD i T.38 nabízí flexibilitu a robustnost, podporuje vše od jednoduchého průchodu audiem až po fax s paketizací a opravou chyb, čímž zajišťuje dlouhodobou životnost této starší služby.

## Klíčové vlastnosti

- Podporuje dva režimy přenosu: přenos v hlasovém pásmu (Voice-Band Data, VBD) a paketizaci podle T.38
- Integrována do architektury IMS s využitím SIP pro řízení relace
- Definuje specifické parametry SDP pro vyjednávání faxových schopností
- Zahrnuje postupy pro propojení s okruhově přepínanými faxovými sítěmi (PSTN)
- Poskytuje záložní mechanismy mezi faxovými režimy pro zvýšení spolehlivosti
- Umožňuje komunikaci faxu skupiny 3 v reálném čase přes mobilní paketové přenosové kanály

## Definující specifikace

- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling

---

📖 **Anglický originál a plná specifikace:** [IFT na 3GPP Explorer](https://3gpp-explorer.com/glossary/ift/)
