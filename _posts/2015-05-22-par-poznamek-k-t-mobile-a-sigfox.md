---
ID: 3000
title: 'Pár poznámek k&nbsp;T-Mobile a&nbsp;SigFox'
author: Patrick Zandl
post_excerpt: ""
layout: post
oldlink: >
  https://www.marigold.cz/item/par-poznamek-k-t-mobile-a-sigfox
published: true
post_date: 2015-05-22 06:19:06
---
<p>Včera ohlásil T-Mobile, že spouští síť pro Internet věcí na technologii SigFox, záhy se ozvaly ČRa, že spouští to samé od LoRa. Tak pár poznámek od mě, neználka se zkoušečkou.</p>

<!--more-->

<p>Obě technologie pracují v bezlicenčním ISM pásmu 868 MHz (906MHz v USA), v němž běží nelicencované krátkodosahové technologie, například část domácích meteostanic, ovládání vrat garáže, ale třeba i wMbus, technologie bezdrátového propojení měřidel. Neběží tam ani bluetooth, ani WiFi, ani energomonitor, ani to s nimi neinterferuje. Technologicky jde o ultraúzké pásmo (UNB), na kterém dlouho pracovala Motorola, než ty lidi vyhodila a oni se udělali pro sebe. Vysílací výkon je omezen na 100 mW, což je taky základ dlouhé výdrže obou technologií v provozu na baterky: vysílají velmi krátký puls dat s minimálním výkonem. Fintou je, jak zvládnout v relativně zahlušeném prostředí tento výkřik přijmout a správně přečíst i na delší, řádově kilometrové vzdálenosti, o tom je těch pár patentů a o tom snad někdy jindy. Na malou knoflíkovou baterku umí SigFox a obecně LoRa technologie (Long Range) pařit rok(y). Je to tím, že se vysílá párkrát denně, jinak zařízení se sítí nekomunikuje (v mobilní sítí komunikuje, i když nepřenáší data uživatele), že to dělá na nízkém výkonu a že vysílá jen velmi krátce. Proto se také přenáší velmi malý datový objem - v případě SigFoxu je to 12 byte. Někde jsem četl, že je to zhruba jako jedna SMS, to ani omylem, ta je desetkrát delší. Do tohoto objemu nacpete jedno číslo a řekněme návěští, co je to za číslo. Moc to nevadí, neposíláte nikomu zamilovaný vzkaz, ale info o tom, že se zapnul požární poplach nebo zásoba v nádrži klesla pod minimum. A posíláte to jinému stroji, který to už pochopí a přeloží do lidského vyjádření třeba v mobilní aplikaci.</p>
<p>K čemu LoRa technologie je? Právě ke stavové komunikaci mezi stroji. Sběr řídkých naměřených hodnot nebo stavů. Problémem jsou limity: SigFox je omezen na 140 zpráv denně, čili zhruba jednou za deset minut. Na něco to stačí - tak často za den vás nevykradou, ale třeba v energomonitoru odesíláme data co minutu, tam už to nestačí. Ale na sběr dat ze stacionárních objektů, například automatů a jiných strojů, to postačuje plně.</p>
<p>Náklady jsou v řádu 15 euro ročně při maximálním využití a klesají při menším, což předurčuje obchodní model: prodat toho hodně, nacpat to všude. Komunikace je zatím jednosměrná, ale pracuje se na variantě, kdy alespoň čip přijme potvrzení, že data došla - to se zatím neděje, proto je taky čip vysílá vícekrát.</p>
<p>Proč se do toho montují operátoři? Protože by jim utíkal business: dosud se soudilo, že je potáhnou M2M aplikace, jenže k nim není u těchto typů klientů, kteří požadují úspornost na energii a nepotřebují mnoho dat, mobilní síť extra vhodná. Takže ledaskdo si montuje na stožáry tyhle LoRa věci - Swisscomm, Bouygues Telecom, KPN a další.  Aby pokryli M2M trh ve větší šířce, vyžili sloupy a zákaznickou bázi. Chytrý tah. Obchodně je ale důležitá jedna věc: mobilní operátoři umí pracovat s trhem, na který je vysoká bariéra vstupu (licence, peníze) a vysoká marže. Trh M2M je trh, kde je nízká bariéra vstupu (bezlicenční, levná technologie s řadou substitutů) a nízká marže vyvážená vysokým počtem uživatelů koncentrovaných ovšem do několika hubů (tedy mnoho zařízení spravovaných jednou firmou). S tím se operátor bude muset porvat a neříkám, že neporve, jen říkám, že je to jiné, než jak byl zvyklý. </p>
<p>Tož tak. Držíme palce. A třeba pro to taky nějaké využití najdeme.</p>
<p> </p>